import os
import re
import time
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Configuration
INPUT_FILE = "ofd_questions.txt"
OUTPUT_DIR = "../database/efd"
TEMPLATE_FILE = "../database/_template.md"
COURSE_NAME = "Estimation, Filtration, and Detection"

def setup_client():
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("Error: OPENROUTER_API_KEY environment variable not set.")
        return None

    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

def parse_questions_from_text(file_path):
    """Parses questions separated by double newlines."""
    if not os.path.exists(file_path):
        print(f"Error: Input file '{file_path}' not found.")
        return []

    with open(file_path, 'r', encoding='utf-8') as f:
        content = f.read()

    # Split by double newlines, strip whitespace, and filter empty entries
    raw_questions = [q.strip() for q in content.split('\n\n') if q.strip()]
    
    # Return formatted list of (id, text)
    return [(i + 1, text) for i, text in enumerate(raw_questions)]

def sanitize_filename(text, question_id):
    # Keep alphanumeric/spaces, lower case, replace spaces/hyphens with underscore
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    text = re.sub(r'[-\s]+', '_', text)
    return f"{question_id:03d}_{text[:50]}" 

def generate_markdown(client, question_id, question_text, template_content):
    prompt = f"""
You are an expert in Estimation, Filtration, and Detection (Signal Processing/Control Theory).
I will provide you with an exam question and a markdown template.
Your task is to fill out the template for this question.

Question: "{question_text}"

Template:
```markdown
{template_content}
```

Instructions:
1. **id**: Use `efd_{question_id:03d}`.
2. **course**: Set to "{COURSE_NAME}".
3. **tags**: Generate 2-4 relevant tags (kebab-case) like 'kalman-filter', 'bayes-estimation', etc.
4. **difficulty**: Estimate 1-5.
5. **type**: Start with 'open'.
6. **Question section**: Insert the question text exactly.
7. **Explanation**: Provide a detailed, educational explanation (at least 200 words). Use LaTeX for math (e.g., $E[X]$).
8. **Related Concepts**: List 2-3 related wiki-links (snake_case).
9. Output **ONLY** the raw markdown content.
"""

    try:
        completion = client.chat.completions.create(
            model="google/gemini-3-flash-preview", 
            messages=[
                {"role": "system", "content": "You are a helpful academic assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        content = completion.choices[0].message.content

        # Cleanup markdown formatting if model includes it
        if content.startswith("```markdown"):
            content = content[11:]
        if content.startswith("```"):
            content = content[3:]
        if content.endswith("```"):
            content = content[:-3]

        return content.strip()
    except Exception as e:
        print(f"Error generating content for Q{question_id}: {e}")
        return None

def main():
    client = setup_client()
    if not client:
        return

    # Ensure template exists or use default backup
    if os.path.exists(TEMPLATE_FILE):
        with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
            template_content = f.read()
    else:
        print(f"Warning: {TEMPLATE_FILE} not found. Using minimal default.")
        template_content = "---\nid: {id}\n---\n# {question}"

    questions = parse_questions_from_text(INPUT_FILE)
    print(f"Found {len(questions)} questions in {INPUT_FILE}.")

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    for i, q_text in questions:
        print(f"Processing Q{i}: {q_text[:60]}...")

        # Pass both text and ID to sanitize_filename
        filename = sanitize_filename(q_text, i) + ".md"
        filepath = os.path.join(OUTPUT_DIR, filename)

        if os.path.exists(filepath):
             print(f"  Skipping Q{i} (File exists: {filename})")
             continue

        content = generate_markdown(client, i, q_text, template_content)

        if content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  Saved to {filename}")
            time.sleep(1) # Slight delay to be polite to API
        else:
            print(f"  Failed to generate Q{i}")

if __name__ == "__main__":
    main()
