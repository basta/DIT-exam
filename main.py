import os
import json
import re
import frontmatter
from datetime import datetime, timedelta
from urllib.parse import quote
from nicegui import ui, app

# --- CONFIGURATION ---
# Change these!
PASSWORD = "Asgard1218"
QUESTIONS_DIR = "./database" 
PROGRESS_FILE = "progress.json"


# --- BACKEND LOGIC ---
def load_progress():
    if os.path.exists(PROGRESS_FILE):
        with open(PROGRESS_FILE, 'r') as f:
            return json.load(f)
    return {}

def save_progress(data):
    with open(PROGRESS_FILE, 'w') as f:
        json.dump(data, f, indent=2)

def get_stats():
    """Calculates score distribution for the histogram."""
    progress = load_progress()
    files = [f for f in os.listdir(QUESTIONS_DIR) if f.endswith('.md') and f != '_template.md']
    
    # Bins: < -20, -20~-1, 0, 1~20, > 20
    # keys allow for sorting and labeling
    bins = {
        'Mastered': 0,
        'Learned': 0,
        'New': 0,
        'Learning': 0,
        'Hard': 0
    }
    
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
            post = frontmatter.load(os.path.join(QUESTIONS_DIR, f))
            q_id = post.metadata.get('id', f)
            
            score = 0
            if q_id in progress:
                score = progress[q_id].get('score', 0)
            
            # Binning
            if score < -20:
                bins['Mastered'] += 1
            elif score < 0:
                bins['Learned'] += 1
            elif score == 0:
                bins['New'] += 1
            elif score <= 20:
                bins['Learning'] += 1
            else:
                bins['Hard'] += 1
                
        except Exception:
            pass

    return bins


def get_due_card():
    """Finds the highest priority card for cramming."""
    progress = load_progress()
    # List all .md files (exclude _template.md)
    files = [f for f in os.listdir(QUESTIONS_DIR) if f.endswith('.md') and f != '_template.md']
    
    candidates = []
    now = datetime.now()
    
    for f in files:
        try:
            post = frontmatter.load(os.path.join(QUESTIONS_DIR, f))
            q_id = post.metadata.get('id', f)
            
            # Cramming Logic: Default to score 0 (neutral)
            card_data = progress.get(q_id, {})
            score = card_data.get('score', 0)
            last_seen_str = card_data.get('last_seen', '2000-01-01T00:00:00')
            last_seen = datetime.fromisoformat(last_seen_str)
            
            candidates.append({
                'id': q_id,
                'file': f,
                'content': post.content,
                'meta': post.metadata,
                'score': score,
                'last_seen': last_seen
            })
        except Exception as e:
            print(f"Error loading {f}: {e}")

    if not candidates:
        return None

    # Sort: Highest Score First (Descending)
    # Tie-breaker: Oldest first
    candidates.sort(key=lambda x: (-x['score'], x['last_seen']))
    
    # Cooldown Check (5 minutes)
    # Try to find the first card that satisfies cooldown
    for card in candidates:
        if (now - card['last_seen']).total_seconds() > 300: # 5 minutes
            return card
            
    # If all cards are in cooldown, just return the highest priority one (cram mode ignores "wait")
    # unless we really want to force a break. But user said "no stop point".
    return candidates[0]

def preprocess_content(text):
    """
    1. Converts Obsidian style ![[image.png]] to standard Markdown.
    2. Ensures block math ($$) has newlines around it to prevent markdown parsing issues.
    """
    if not text:
        return ""

    # 1. Fix Images

    pattern_img = r'!?\[\[(.*?)(?:\|.*?)?\]\]'
    text = re.sub(pattern_img, lambda m: f'![{m.group(1)}](/media/{quote(m.group(1))})', text)

    pattern_math = r'([ \t]*)(\$\$[\s\S]*?\$\$)'
    text = re.sub(pattern_math, r'\n\1\2\n', text)

    # 3. Format Options
    pattern_opts = r'(?m)^([A-Za-z])\) (.*)'
    text = re.sub(pattern_opts, r'- **\1)** \2', text)

    # 3. Fix List Spacing
    # Ensure there is a blank line before a list starts. 
    # Finds a newline followed by a bullet OR a number, preceded by non-newline characters.
    # We insert an extra newline.
    # Matches: "- item", "* item", "1. item", "10. item"
    pattern_list = r'(?<=[^\n])\n(\s*(?:[-*]|\d+\.) )'
    text = re.sub(pattern_list, r'\n\n\1', text)


    # 4. Protect LaTeX from Markdown
    # Markdown often interprets subscripts like $L_x$ as italic $L<em>x$.
    # We find all math blocks and escape _ and * inside them.
    def protect_math(match):
        content = match.group(0)
        # Check if it's already protected or simple
        content = content.replace('_', '\\_') # Escape underscore
        content = content.replace('*', '\\*') # Escape asterisk
        return content

    # Regex for both inline $...$ and block $$...$$
    # We must be careful not to match across newlines for inline, but yes for block.
    # Pattern: $$...$$ OR $...$
    pattern_math_content = r'(\$\$[\s\S]*?\$\$|\$[^\n$]*?\$)'
    text = re.sub(pattern_math_content, protect_math, text)

    return text

# --- UI LOGIC ---
@ui.page('/')
def main_page():
    # 1. AUTHENTICATION CHECK
    # We use a simple container to swap between login and study views
    content_area = ui.column().classes('w-full max-w-3xl mx-auto p-4')

    def render_login():
        content_area.clear()
        with content_area:
            ui.label('🔒 Restricted Area').classes('text-2xl font-bold mb-4')
            pwd = ui.input('Password', password=True).classes('w-full')
            
            def check_pass():
                if pwd.value == PASSWORD:
                    render_study()
                else:
                    ui.notify('Wrong password', color='negative')
            
            ui.button('Enter', on_click=check_pass).classes('w-full')
            pwd.on('keydown.enter', check_pass)

    def render_study():
        content_area.clear()
        
        # Fetch Data
        card = get_due_card()
        
        if not card:
            with content_area:
                ui.label('🎉 All Caught Up!').classes('text-3xl font-bold text-green-500')
                ui.label('No questions due right now.').classes('text-lg')
                ui.button('Refresh', on_click=render_study).classes('mt-4')
            return

        # Render Card
        with content_area:
            # Header Info
            stats = get_stats() 
            # Stats Chart Data
            # Define colors for each category
            # Mastered (Deep Green), Learned (Green), New (Blue), Learning (Orange), Hard (Red)
            colors = ['#15803d', '#4ade80', '#60a5fa', '#fb923c', '#ef4444']
            x_data = list(stats.keys())
            y_data = list(stats.values())
            
            # Construct series data with individual styles if needed, 
            # but simpler to use itemStyle callback or just a list of colors if each bar is a category.
            # ECharts doesn't map array of colors to categories automatically in headers unless configured.
            # Best way: 'data': [{'value': v, 'itemStyle': {'color': c}} ...]
            
            chart_data = []
            for i, (k, v) in enumerate(stats.items()):
                chart_data.append({
                    'value': v,
                    'itemStyle': {'color': colors[i]}
                })

            with ui.row().classes('w-full justify-between items-center mb-4'):
                ui.label(card['meta'].get('course', 'General')).classes('text-sm font-bold uppercase tracking-wider text-gray-500')
                
                with ui.row().classes('items-center gap-4 flex-1 justify-end'):
                     # Echart Histogram
                    ui.echart({
                        'grid': {'top': 20, 'bottom': 20, 'left': 5, 'right': 5, 'containLabel': True},
                        'xAxis': {
                            'type': 'category', 
                            'data': x_data, 
                            'show': True,
                            'axisLine': {'show': False},
                            'axisTick': {'show': False},
                            'axisLabel': {'interval': 0, 'fontSize': 10, 'color': '#666'}
                        },
                        'yAxis': {'type': 'value', 'show': False},
                        'series': [{
                            'data': chart_data, 
                            'type': 'bar', 
                            'label': {'show': True, 'position': 'top', 'color': '#333'}
                        }]
                    }).classes('w-64 h-32') # Increased size slightly to fit labels

                    # Tags
                    with ui.row().classes('items-center gap-1'):
                        for tag in card['meta'].get('tags', []):
                            ui.label(f'#{tag}').classes('text-xs bg-gray-200 px-2 py-1 rounded')


            # QUESTION CONTENT
            # We process the text to fix image links before rendering
            processed_q = preprocess_content(card['content'].split('# Solution')[0]) # Show only up to Solution
            ui.markdown(processed_q).classes('prose w-full max-w-none')

            # Action Area (Hidden Answer)
            answer_area = ui.column().classes('w-full mt-8 border-t pt-8 hidden')
            
            with answer_area:
                ui.label('Solution').classes('text-xl font-bold mb-4')
                # Extract solution part
                if '# Solution' in card['content']:
                    solution_text = card['content'].split('# Solution')[1]
                    ui.markdown(preprocess_content(solution_text)).classes('prose w-full max-w-none')
                else:
                    ui.label('No solution text found in file.').classes('text-red-400')

                # Rating Buttons
                ui.label('How hard was this?').classes('mt-8 font-bold')
                with ui.row().classes('w-full gap-4 mt-2'):
                    def submit_review(rating):
                        # Cramming Logic (Priority Queue)
                        current_score = card['score']
                        
                        if rating == 'hard':
                            # Shoot to top
                            new_score = current_score + 20
                        elif rating == 'good':
                            # Drop slightly
                            new_score = current_score - 5
                        else: # easy
                            # Drop significantly
                            new_score = current_score - 15
                        
                        # Save
                        prog = load_progress()
                        prog[card['id']] = {
                            'score': new_score,
                            'last_seen': datetime.now().isoformat()
                        }
                        save_progress(prog)
                        
                        # Next Card
                        ui.notify(f'Priority Updated (Score: {new_score})', color='positive')
                        render_study()

                    ui.button('Hard (Reset)', on_click=lambda: submit_review('hard')).props('color=red').classes('flex-1')
                    ui.button('Good', on_click=lambda: submit_review('good')).props('color=orange').classes('flex-1')
                    ui.button('Easy', on_click=lambda: submit_review('easy')).props('color=green').classes('flex-1')

            # Show Answer Button
            show_btn = ui.button('Show Answer', on_click=lambda: (show_btn.set_visibility(False), answer_area.classes(remove='hidden'))).classes('w-full mt-8')
            
            # Re-render LaTeX
            ui.run_javascript('if (window.MathJax) window.MathJax.typeset();')

    # Initial Render
    render_login()

# --- SERVER SETUP ---
# This exposes your questions folder so images can be loaded via /media/filename.png
app.add_static_files('/media', QUESTIONS_DIR)

# Enable LaTeX support in the head
ui.add_head_html('''
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
''', shared=True)

if __name__ in {"__main__", "__mp_main__"}:
    # Remove 'native' to run in browser instead of a window
    # port=8080 makes it accessible on your server
    ui.run(title="Cybernetics Study", port=8080, show=False)