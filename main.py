import os
import json
import random
import re
import frontmatter
from datetime import datetime, timedelta
from urllib.parse import quote
from nicegui import ui, app

# --- CONFIGURATION ---
QUESTIONS_DIR = "./database"
USERS_DIR = "./users"
INVALID_OPTION_MARKERS = ["N/A"]


def get_tracks():
    """Scans QUESTIONS_DIR for subdirectories (tracks)."""
    tracks = []
    try:
        items = os.listdir(QUESTIONS_DIR)
    except FileNotFoundError:
        return []

    for item in items:
        full_path = os.path.join(QUESTIONS_DIR, item)
        if os.path.isdir(full_path) and not item.startswith("."):
            # Check for info.json
            info_path = os.path.join(full_path, "info.json")
            track_info = {
                "id": item,
                "name": item,  # Fallback
                "description": "",
                "path": full_path,
            }
            if os.path.exists(info_path):
                try:
                    with open(info_path, "r") as f:
                        data = json.load(f)
                        track_info.update(data)
                        # Ensure path is correct even if json says otherwise?
                        # Usually json might have 'id' but we want 'path' to be real.
                        track_info["path"] = full_path
                except Exception as e:
                    print(f"Error reading {info_path}: {e}")

            tracks.append(track_info)

    # Sort by name
    tracks.sort(key=lambda x: x["name"])
    return tracks


# --- BACKEND LOGIC ---
import hashlib


def get_user_hash(password):
    return hashlib.sha256(password.encode()).hexdigest()


def get_progress_file(user_hash):
    return os.path.join(USERS_DIR, f"{user_hash}.json")


def load_progress(user_hash):
    pfile = get_progress_file(user_hash)
    if os.path.exists(pfile):
        with open(pfile, "r") as f:
            return json.load(f)
    return {}


def save_progress(user_hash, data):
    pfile = get_progress_file(user_hash)
    with open(pfile, "w") as f:
        json.dump(data, f, indent=2)


def get_stats(progress, track_dir):
    """Calculates score distribution for the histogram."""
    # Use the specific track directory
    try:
        files = [
            f
            for f in os.listdir(track_dir)
            if f.endswith(".md") and f != "_template.md"
        ]
    except FileNotFoundError:
        return {"Mastered": 0, "Learned": 0, "New": 0, "Learning": 0, "Hard": 0}

    # Bins: < -20, -20~-1, 0, 1~20, > 20
    # keys allow for sorting and labeling
    bins = {"Mastered": 0, "Learned": 0, "New": 0, "Learning": 0, "Hard": 0}

    # We explicitly check every file to ensure "New" (score 0) is counted correctly
    for f in files:
        try:
            # We assume ID = filename for speed if not in progress
            # (To be perfectly accurate we'd need to load every file,
            # but usually ID defaults to filename if no ID in frontmatter)

            # Optimization: Check if filename is in progress keys directly?
            # Progress keys are IDs.
            # If we want to be safe, we have to follow get_due_card logic,
            # but that is slow for 1000s of files.
            # Let's try to map progress entries to files they belong to?
            # No, that's reverse.

            # Simple approach: Load frontmatter (as in previous code)
            # This is acceptable for hundreds of files.
            post = frontmatter.load(os.path.join(track_dir, f))
            q_id = post.metadata.get("id", f)

            score = 0
            if q_id in progress:
                score = progress[q_id].get("score", 0)

            # Binning
            if score < -20:
                bins["Mastered"] += 1
            elif score < 0:
                bins["Learned"] += 1
            elif score == 0:
                bins["New"] += 1
            elif score <= 20:
                bins["Learning"] += 1
            else:
                bins["Hard"] += 1

        except Exception:
            pass

    return bins


    return bins


def extract_question_text(content):
    """Extracts the question text from the markdown content."""
    lines = content.split('\n')
    question_lines = []
    capture = False
    
    for line in lines:
        if line.strip().startswith("# Question"):
            capture = True
            continue
        
        if capture:
            # Stop at the next header or separator
            if line.strip().startswith("#") or line.strip().startswith("---"):
                break
            # Skip empty lines at the start? No, strip later.
            question_lines.append(line)
            
    text = "\n".join(question_lines).strip()
    
    # If no "# Question" header found, or empty, maybe return the whole thing or first part?
    # Fallback to first non-empty paragraph if "Question" header is missing
    if not text and not capture:
        # Just take the first paragraph
        paras = content.split('\n\n')
        if paras:
             text = paras[0].strip()

    return text


def extract_solution_text(content):
    """Extracts the solution text from the markdown content."""
    parts = content.split("# Solution")
    if len(parts) > 1:
        # Return everything after "# Solution"
        return parts[1].strip()
    return "No solution text found."


def extract_related_topic(content):
    """Extracts the first related topic from the markdown content."""
    # Look for "## Related Concepts"
    parts = content.split("## Related Concepts")
    if len(parts) > 1:
        # Look for [[Topic]]
        match = re.search(r"\[\[(.*?)\]\]", parts[1])
        if match:
            return match.group(1)
    
    # Fallback to tags or None
    return None


def get_all_questions(progress, track_dir):
    """Fetches all questions with status for the list view."""
    try:
        files = [
            f
            for f in os.listdir(track_dir)
            if f.endswith(".md") and f != "_template.md"
        ]
    except FileNotFoundError:
        return []

    questions = []
    for f in files:
        try:
            post = frontmatter.load(os.path.join(track_dir, f))
            q_id = post.metadata.get("id", f)

            score = 0
            if q_id in progress:
                score = progress[q_id].get("score", 0)

            # Determine status
            if score < -20:
                status = "Mastered"
            elif score < 0:
                status = "Learned"
            elif score == 0:
                status = "New"
            elif score <= 20:
                status = "Learning"
            else:
                status = "Hard"
            
            # Parse Question Text
            q_text = extract_question_text(post.content)
            # Truncate for list view
            q_preview = q_text[:150] + "..." if len(q_text) > 150 else q_text

            # Parse Solution Text
            sol_text = extract_solution_text(post.content)

            # Parse Topic
            topic = extract_related_topic(post.content)
            if not topic:
                # Fallback to metadata topic if available
                topic = post.metadata.get("topic", "")
                if isinstance(topic, list) and topic:
                     topic = topic[0]

            questions.append(
                {
                    "id": q_id,
                    "file": f,
                    "content": post.content,
                    "question_text": q_preview, # Use this in UI
                    "solution_text": sol_text,
                    "topic": topic,
                    "meta": post.metadata,
                    "score": score,
                    "status": status,
                }
            )
        except Exception as e:
            print(f"Error loading {f}: {e}")

    # Sort by ID (usually numeric)
    # Try to parse ID as int if possible for better sorting
    def sort_key(x):
        try:
            return int(x["id"])
        except ValueError:
            return x["id"]

    questions.sort(key=sort_key)
    return questions


def get_due_card(progress, track_dir):
    """Finds the highest priority card for cramming."""
    # List all .md files (exclude _template.md)
    try:
        files = [
            f
            for f in os.listdir(track_dir)
            if f.endswith(".md") and f != "_template.md"
        ]
    except FileNotFoundError:
        return None

    candidates = []
    now = datetime.now()

    for f in files:
        try:
            post = frontmatter.load(os.path.join(track_dir, f))
            q_id = post.metadata.get("id", f)

            # Cramming Logic: Default to score 0 (neutral)
            card_data = progress.get(q_id, {})
            score = card_data.get("score", 0)
            last_seen_str = card_data.get("last_seen", "2000-01-01T00:00:00")
            last_seen = datetime.fromisoformat(last_seen_str)

            # Calculate Unlock Time
            # If last_seen is future (Skip), that's the unlock time.
            # Else, enforce 5 minute cooldown.
            if last_seen > now:
                unlock_time = last_seen
            else:
                unlock_time = last_seen + timedelta(minutes=5)

            candidates.append(
                {
                    "id": q_id,
                    "file": f,
                    "content": post.content,
                    "meta": post.metadata,
                    "score": score,
                    "last_seen": last_seen,
                    "unlock_time": unlock_time,
                }
            )
        except Exception as e:
            print(f"Error loading {f}: {e}")

    if not candidates:
        return None

    # Shuffle candidates to ensure random selection for ties
    random.shuffle(candidates)

    # 1. Filter Ready Candidates
    ready = [c for c in candidates if c["unlock_time"] <= now]

    if ready:
        # Sort Ready: Highest Score First
        ready.sort(key=lambda x: (-x["score"], x["last_seen"]))
        return ready[0]

    # 2. Fallback: None ready -> Closest to unlocking
    candidates.sort(key=lambda x: x["unlock_time"])
    return candidates[0]


def preprocess_content(text):
    """
    1. Converts Obsidian style ![[image.png]] to standard Markdown.
    2. Ensures block math ($$) has newlines around it to prevent markdown parsing issues.
    """
    if not text:
        return ""

    # 1. Fix Images

    pattern_img = r"!?\[\[(.*?)(?:\|.*?)?\]\]"
    text = re.sub(
        pattern_img, lambda m: f"![{m.group(1)}](/media/{quote(m.group(1))})", text
    )

    pattern_math = r"([ \t]*)(\$\$[\s\S]*?\$\$)"
    text = re.sub(pattern_math, r"\n\1\2\n", text)

    # 3. Format Options
    pattern_opts = r"(?m)^([A-Za-z])\) (.*)"
    text = re.sub(pattern_opts, r"- **\1)** \2", text)

    # 3. Fix List Spacing
    # Ensure there is a blank line before a list starts.
    # Finds a newline followed by a bullet OR a number, preceded by non-newline characters.
    # We insert an extra newline.
    # Matches: "- item", "* item", "1. item", "10. item"
    pattern_list = r"(?<=[^\n])\n(\s*(?:[-*]|\d+\.) )"
    text = re.sub(pattern_list, r"\n\n\1", text)

    # 4. Protect LaTeX from Markdown
    # Markdown often interprets subscripts like $L_x$ as italic $L<em>x$.
    # We find all math blocks and escape _ and * inside them.
    def protect_math(match):
        content = match.group(0)
        # Check if it's already protected or simple
        content = content.replace("_", "\\_")  # Escape underscore
        content = content.replace("*", "\\*")  # Escape asterisk
        return content

    # Regex for both inline $...$ and block $$...$$
    # We must be careful not to match across newlines for inline, but yes for block.
    # Pattern: $$...$$ OR $...$
    pattern_math_content = r"(\$\$[\s\S]*?\$\$|\$[^\n$]*?\$)"
    text = re.sub(pattern_math_content, protect_math, text)

    # 5. Hide Options if Invalid
    # Finds '## Options' and removes the section if it contains any invalid marker.
    # Uses a lookahead to stop at the next header or '---' separator.
    pattern_options = r"(?m)^## Options\s*(.*?)(?=^---|^(?:# )|\Z)"

    def check_and_remove(match):
        content = match.group(1)
        for marker in INVALID_OPTION_MARKERS:
            if marker in content:
                return ""  # Remove section
        return match.group(0)

    text = re.sub(pattern_options, check_and_remove, text, flags=re.DOTALL)

    return text


# --- UI LOGIC ---
@ui.page("/")
def main_page():
    # 1. AUTHENTICATION CHECK
    # We use a simple container to swap between login and study views
    content_area = ui.column().classes("w-full max-w-3xl mx-auto p-4")

    def render_login():
        content_area.clear()
        with content_area:
            ui.label("👋 Welcome!").classes("text-2xl font-bold mb-4")
            ui.markdown(
                "Enter any **passkey** or **phrase** to log in.<br>"
                "If this is your first time, a new user profile is created automatically.<br>"
                "To resume your progress later, simply use the same passkey."
            ).classes("text-gray-600 mb-6 text-sm")
            pwd = ui.input("Passkey", password=True).classes("w-full")

            def check_pass():
                if pwd.value:
                    user_hash = get_user_hash(pwd.value)
                    app.storage.user['user_hash'] = user_hash
                    render_track_selection(user_hash)
                else:
                    ui.notify("Please enter a passkey", color="warning")

            ui.button("Enter", on_click=check_pass).classes("w-full")
            pwd.on("keydown.enter", check_pass)

    def render_track_selection(user_hash):
        content_area.clear()
        tracks = get_tracks()

        with content_area:
            with ui.row().classes("w-full justify-between items-center mb-6"):
                ui.label("Select a Track").classes("text-2xl font-bold")
                ui.button("Logout", on_click=lambda: (app.storage.user.clear(), render_login())).props("flat color=grey")


            if not tracks:
                ui.label("No tracks found.").classes("text-red-500")
                return

            with ui.column().classes("w-full gap-4"):
                for track in tracks:
                    with (
                        ui.card()
                        .classes("w-full cursor-pointer hover:bg-gray-50")
                        .on("click", lambda t=track: render_study(user_hash, t))
                    ):
                        ui.label(track["name"]).classes("text-lg font-bold")
                        if track["description"]:
                            ui.label(track["description"]).classes(
                                "text-sm text-gray-600"
                            )

    def render_question_list(user_hash, track):
        content_area.clear()

        # Load Progress
        progress = load_progress(user_hash)
        questions = get_all_questions(progress, track["path"])

        with content_area:
            # Header
            with ui.row().classes(
                "w-full justify-between items-center mb-6 border-b pb-4"
            ):
                with ui.row().classes("items-center gap-4"):
                    ui.button(on_click=lambda: render_study(user_hash, track)).props(
                        "flat icon=arrow_back round"
                    )
                    ui.label(track["name"]).classes("text-xl font-bold")

                with ui.row().classes("items-center gap-2"):
                    ui.button("Switch Track", on_click=lambda: render_track_selection(user_hash)).props(
                         "outline size=sm"
                    )
                    # ui.button(icon="dark_mode").props("flat round") # Future: Dark mode toggle

            # Search/Filter Bar
            with ui.row().classes("w-full mb-4 gap-4"):
                search = ui.input("Search questions, tags, or IDs...").props(
                    "outlined dense rounded"
                ).classes("flex-1")
                
                # Simple Status Filter (Dropdown)
                status_filter = ui.select(
                    ["All Statuses", "Mastered", "Learned", "New", "Learning", "Hard"],
                    value="All Statuses",
                ).props("outlined dense options-dense")
                
                # Update filter logic to include status
                def filter_full():
                     q = search.value.lower()
                     s = status_filter.value
                     
                     filtered = []
                     for item in questions:
                         # Text search
                         match_text = (q in item["content"].lower() or 
                                       q in str(item["id"]).lower() or 
                                       q in str(item["meta"]).lower())
                         
                         # Status search
                         match_status = (s == "All Statuses" or item["status"] == s)
                         
                         if match_text and match_status:
                             filtered.append(item)
                     
                     list_container.clear()
                     with list_container:
                         render_list_items(filtered)

                search.on("input", filter_full)
                status_filter.on_value_change(filter_full)


            # Table Header
            with ui.row().classes("w-full px-4 py-2 bg-gray-50 border-b text-xs font-bold text-gray-500 uppercase tracking-wider"):
                ui.label("ID").classes("w-16")
                ui.label("Question").classes("flex-1")
                ui.label("Topic").classes("w-32")
                ui.label("Status").classes("w-24 text-center")
                ui.label("Action").classes("w-16 text-right")

            # Questions List
            list_container = ui.column().classes("w-full gap-0")

            def render_list_items(items):
                if not items:
                    ui.label("No questions found matching criteria.").classes("p-4 text-gray-500 italic")
                    return

                def lazy_load_solution(container, question):
                     # Check if already loaded
                     if list(container):
                         return
                     
                     with container:
                        ui.label("Solution").classes("text-xs font-bold text-gray-500 uppercase mb-2")
                        processed_sol = preprocess_content(question["solution_text"])
                        ui.markdown(processed_sol).classes("prose w-full max-w-none text-sm")
                        # Add Re-render Latex call
                        ui.run_javascript("if (window.MathJax) window.MathJax.typeset();")

                for q in items:
                    # Use expansion for inline answer
                    # We use a custom header to mimic the previous table row layout
                    # NOTE: Do NOT bind on_value_change here with a lambda that needs the content_container 
                    # because content_container is not created yet. We bind it AFTER creation below.
                    with ui.expansion().classes("w-full border-b hover:bg-gray-50 transition-colors group") as expansion:
                        with expansion.add_slot("header"):
                             with ui.row().classes("w-full items-center"):
                                # ID
                                ui.label(f"#{q['id']}").classes("w-16 text-xs text-gray-400 font-mono")
                                
                                # Question
                                question_text = q["question_text"]
                                if "title" in q["meta"]:
                                     question_text = q["meta"]["title"]
                                     
                                with ui.column().classes("flex-1"):
                                     ui.label(question_text).classes("text-sm font-medium text-blue-600")

                                # Topic
                                topic = q["topic"]
                                
                                ui.label(str(topic)).classes("w-32 text-xs truncate bg-indigo-50 text-indigo-700 px-2 py-1 rounded-full text-center")

                                # Status
                                status_colors = {
                                    "Mastered": "bg-green-100 text-green-700",
                                    "Learned": "bg-green-50 text-green-600",
                                    "New": "bg-gray-100 text-gray-600",
                                    "Learning": "bg-yellow-100 text-yellow-700",
                                    "Hard": "bg-red-100 text-red-700"
                                }
                                ui.label(q["status"]).classes(f"w-24 text-center text-xs px-2 py-1 rounded-full font-medium {status_colors.get(q['status'], 'bg-gray-100')}")

                                # Action
                                with ui.row().classes("w-16 justify-end"):
                                     # Edit/View icons
                                     # To stop propagation, using standard Quasar/Vue modifiers is tricky in Python without 'args'.
                                     # However, we can just use the standard prevent default approach if the event supports it, 
                                     # but pure NiceGUI/Quasar events often don't expose preventDefault easily in vanilla handlers.
                                     # A simpler way is to wrapping the button in a div that stops propagation? 
                                     # OR better: ui.button().on('click.stop', ...) modifier which Quasar supports.
                                     # We use .on('click', ..., ['stop', 'prevent']) to ensuring no bubbling.
                                     ui.button(icon="open_in_new").on('click', lambda e, x=q: render_study(user_hash, track, force_card_file=x['file']), ['stop', 'prevent']).props("flat round dense size=sm color=grey").tooltip("Open Full Card")
                        
                        # Expansion Content (Answer) - Lazy Container
                        content_container = ui.column().classes("w-full bg-gray-50 p-4 border-t")
                        
                        # Correctly bind the handler now that content_container exists
                        expansion.on_value_change(lambda e, c=content_container, x=q: lazy_load_solution(c, x) if e.value else None)
            
            with list_container:
                render_list_items(questions)


    def render_study(user_hash, track, force_card_file=None):
        content_area.clear()

        # Load Progress
        progress = load_progress(user_hash)

        # Header with Track Name and Switch Button
        with content_area:
            with ui.row().classes(
                "w-full justify-between items-center mb-6 border-b pb-4"
            ):
                with ui.row().classes("items-center gap-2"):
                     ui.button(icon="arrow_back", on_click=lambda: render_track_selection(user_hash)).props("flat round dense")
                     ui.label(track["name"]).classes("text-xl font-bold")
                
                with ui.row().classes("gap-2"):
                    ui.button("Switch Track", on_click=lambda: render_track_selection(user_hash)).props("outline size=sm")
                    ui.button("List View", on_click=lambda: render_question_list(user_hash, track)).props("unelevated color=blue size=sm")

        # Fetch Data
        card = None
        if force_card_file:
             try:
                f_path = os.path.join(track["path"], force_card_file)
                post = frontmatter.load(f_path)
                q_id = post.metadata.get("id", force_card_file)
                card_data = progress.get(q_id, {})
                score = card_data.get("score", 0)
                card = {
                    "id": q_id,
                    "file": force_card_file,
                    "content": post.content,
                    "meta": post.metadata,
                    "score": score,
                }
             except Exception as e:
                print(f"Error loading {force_card_file}: {e}")
        
        if not card:
            # Fallback to due card if generic study or load failed
            card = get_due_card(progress, track["path"])

        if not card:
            with content_area:
                ui.label("🎉 All Caught Up!").classes(
                    "text-3xl font-bold text-green-500"
                )
                ui.label("No questions due right now.").classes("text-lg")
                ui.button(
                    "Refresh", on_click=lambda: render_study(user_hash, track)
                ).classes("mt-4")
                ui.button(
                    "Refresh", on_click=lambda: render_study(user_hash, track)
                ).classes("mt-4")
                ui.button("Logout", on_click=lambda: (app.storage.user.clear(), render_login())).props("color=grey").classes(
                    "mt-4"
                )
            return


        # Render Card
        with content_area:
            # Header Info
            stats = get_stats(progress, track["path"])
            # Stats Chart Data
            # Define colors for each category
            # Mastered (Deep Green), Learned (Green), New (Blue), Learning (Orange), Hard (Red)
            colors = ["#15803d", "#4ade80", "#60a5fa", "#fb923c", "#ef4444"]
            x_data = list(stats.keys())
            y_data = list(stats.values())

            # Construct series data with individual styles if needed,
            # but simpler to use itemStyle callback or just a list of colors if each bar is a category.
            # ECharts doesn't map array of colors to categories automatically in headers unless configured.
            # Best way: 'data': [{'value': v, 'itemStyle': {'color': c}} ...]

            chart_data = []
            for i, (k, v) in enumerate(stats.items()):
                chart_data.append({"value": v, "itemStyle": {"color": colors[i]}})

            with ui.row().classes("w-full justify-between items-center mb-4"):
                with ui.column().classes("gap-0"):
                    with ui.row():
                        ui.label(card["meta"].get("course", "General")).classes(
                            "text-sm font-bold uppercase tracking-wider text-gray-500"
                        )
                        ui.button(
                            "Switch Track",
                            on_click=lambda: render_track_selection(user_hash),
                        ).props("outline size=sm")
                    with ui.row().classes("items-center gap-2"):
                        ui.label(f"{card['file']} • {card['score']}").classes(
                            "text-xs text-gray-400"
                        )
                        github_url = f"https://github.com/basta/DIT-exam/blob/master/database/{track['id']}/{card['file']}"
                        ui.button(icon="open_in_new").props(
                            f'flat round size=xs density=compact color=grey href="{github_url}" target="_blank"'
                        ).tooltip("Open in GitHub")
                        
                        if force_card_file:
                             ui.label("(Preview Mode)").classes("text-xs bg-yellow-100 text-yellow-800 px-2 rounded")

                with ui.row().classes("items-center gap-4 flex-1 justify-end"):
                    # Echart Histogram
                    ui.echart(
                        {
                            "grid": {
                                "top": 20,
                                "bottom": 20,
                                "left": 5,
                                "right": 5,
                                "containLabel": True,
                            },
                            "xAxis": {
                                "type": "category",
                                "data": x_data,
                                "show": True,
                                "axisLine": {"show": False},
                                "axisTick": {"show": False},
                                "axisLabel": {
                                    "interval": 0,
                                    "fontSize": 10,
                                    "color": "#666",
                                },
                            },
                            "yAxis": {"type": "value", "show": False},
                            "series": [
                                {
                                    "data": chart_data,
                                    "type": "bar",
                                    "label": {
                                        "show": True,
                                        "position": "top",
                                        "color": "#333",
                                    },
                                }
                            ],
                        }
                    ).classes("w-64 h-32")  # Increased size slightly to fit labels

                    # Tags
                    # with ui.row().classes("items-center gap-1"):
                    #     for tag in card["meta"].get("tags", []):
                    #         ui.label(f"#{tag}").classes(
                    #             "text-xs bg-gray-200 px-2 py-1 rounded"
                    #         )

            # QUESTION CONTENT
            # We process the text to fix image links before rendering
            processed_q = preprocess_content(
                card["content"].split("# Solution")[0]
            )  # Show only up to Solution
            ui.markdown(processed_q).classes("prose w-full max-w-none")

            # Action Area (Hidden Answer)
            answer_area = ui.column().classes("w-full mt-8 border-t pt-8 hidden")

            with answer_area:
                ui.label("Solution").classes("text-xl font-bold mb-4")
                # Extract solution part
                if "# Solution" in card["content"]:
                    solution_text = card["content"].split("# Solution")[1]
                    ui.markdown(preprocess_content(solution_text)).classes(
                        "prose w-full max-w-none"
                    )
                else:
                    ui.label("No solution text found in file.").classes("text-red-400")

                # Rating Buttons
                ui.label("How hard was this?").classes("mt-8 font-bold")
                with ui.row().classes("w-full gap-4 mt-2"):

                    def submit_review(rating):
                        # Cramming Logic (Priority Queue)
                        current_score = card["score"]

                        next_seen = datetime.now()

                        if rating == "hard":
                            # Shoot to top
                            new_score = current_score + 20
                        elif rating == "good":
                            # Drop slightly
                            new_score = current_score - 5
                        elif rating == "easy":
                            # Drop significantly
                            new_score = current_score - 15
                        elif rating == "skip":
                            # Pause for 10 minutes
                            new_score = current_score
                            next_seen = datetime.now() + timedelta(minutes=10)
                        else:
                            new_score = current_score

                        # Save
                        prog = load_progress(user_hash)
                        prog[card["id"]] = {
                            "score": new_score,
                            "last_seen": next_seen.isoformat(),
                        }
                        save_progress(user_hash, prog)

                        # Next Card
                        ui.notify(
                            f"Priority Updated (Score: {new_score})", color="positive"
                        )
                        render_study(user_hash, track)

                    ui.button(
                        "Hard (Reset)", on_click=lambda: submit_review("hard")
                    ).props("color=red").classes("flex-1")
                    ui.button("Good", on_click=lambda: submit_review("good")).props(
                        "color=orange"
                    ).classes("flex-1")
                    ui.button("Easy", on_click=lambda: submit_review("easy")).props(
                        "color=green"
                    ).classes("flex-1")
                    ui.button(
                        "Skip (10m)", on_click=lambda: submit_review("skip")
                    ).props("color=grey").classes("flex-1")

            # Show Answer Button
            show_btn = ui.button(
                "Show Answer",
                on_click=lambda: (
                    show_btn.set_visibility(False),
                    answer_area.classes(remove="hidden"),
                ),
            ).classes("w-full mt-8")

            # Re-render LaTeX
            ui.run_javascript("if (window.MathJax) window.MathJax.typeset();")

    # Initial Render
    # Check for persisting session
    if 'user_hash' in app.storage.user:
        render_track_selection(app.storage.user['user_hash'])
    else:
        render_login()



app.add_static_files("/media", QUESTIONS_DIR)

# Enable LaTeX support in the head
ui.add_head_html(
    """
    <script>
        window.MathJax = {
            tex: {
                inlineMath: [['$', '$']],
                displayMath: [['$$', '$$']]
            },
            svg: { fontCache: 'global' }
        };
    </script>
    <script async src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js"></script>
""",
    shared=True,
)

if __name__ in {"__main__", "__mp_main__"}:
    # Remove 'native' to run in browser instead of a window
    # port=8080 makes it accessible on your server
    # Remove 'native' to run in browser instead of a window
    # port=8080 makes it accessible on your server
    ui.run(title="Cybernetics Study", port=8080, show=False, storage_secret="your-secret-key-here")

