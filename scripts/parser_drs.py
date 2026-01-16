import os
import re
import json
import time
from bs4 import BeautifulSoup
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

# Configuration
HTML_FILE = "database/drs/_question_list.html"
OUTPUT_DIR = "database/drs"
TEMPLATE_FILE = "database/_template.md"
COURSE_NAME = "Dynamics and Control of Networks"

def setup_client():
    api_key = os.environ.get("OPENROUTER_API_KEY")
    if not api_key:
        print("Error: OPENROUTER_API_KEY environment variable not set.")
        return None
    
    return OpenAI(
        base_url="https://openrouter.ai/api/v1",
        api_key=api_key,
    )

def parse_questions(html_path):
    with open(html_path, 'r', encoding='utf-8') as f:
        soup = BeautifulSoup(f, 'html.parser')
    
    questions = []
    
    content_div = soup.find('div', class_='no-overflow')
    if content_div:
        ol = content_div.find('ol')
        if ol:
            for i, li in enumerate(ol.find_all('li')):
                text = li.get_text(strip=True)
                if text:
                    questions.append((i + 1, text))
    
    return questions

def sanitize_filename(text, question_id):
    # Keep only alphanumeric and spaces, then replace spaces with underscores, lower case
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    text = re.sub(r'[-\s]+', '_', text)
    # Include ID to ensure uniqueness and increase length limit
    return f"{question_id:03d}_{text[:100]}"

def generate_markdown(client, question_id, question_text, template_content):
    prompt = f"""
You are an expert in Network Dynamics and Control.
I will provide you with an exam question and a markdown template.
Your task is to fill out the template for this question.

Question: "{question_text}"

Template:
```markdown
{template_content}
```

Instructions:
1. **id**: Use `drs_{question_id:03d}`.
2. **course**: Set to "{COURSE_NAME}".
3. **tags**: Generate 2-4 relevant tags (kebab-case).
4. **difficulty**: Estimate 1-5 (1=Easy, 5=Hard).
5. **type**: Start with 'open'.
6. **Question section**: Insert the question text exactly.
7. **Explanation**: Provide a detailed, correct, and educational explanation (at least 200 words). Use LaTeX mathematical formatting where appropriate (e.g., $x^2$).
8. **Related Concepts**: List 2-3 related wiki-links concept names (snake_case).
9. Output **ONLY** the raw markdown content. Do not include triple backticks block markers if not necessary, but if you do, I will strip them.
"""

    try:
        completion = client.chat.completions.create(
            model="google/gemini-3-flash-preview", # Using a cost-effective but capable model
            messages=[
                {"role": "system", "content": "You are a helpful academic assistant."},
                {"role": "user", "content": prompt}
            ]
        )
        content = completion.choices[0].message.content
        
        # Strip markdown code blocks if present
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

    # Read template
    with open(TEMPLATE_FILE, 'r', encoding='utf-8') as f:
        template_content = f.read()

    questions = parse_questions(HTML_FILE)
    print(f"Found {len(questions)} questions.")

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
    for i, q_text in questions:
        print(f"Processing Q{i}: {q_text[:60]}...")
        
        # Create a semantic filename
        filename = sanitize_filename(q_text[:30]) + ".md"
        filepath = os.path.join(OUTPUT_DIR, filename)
        
        if os.path.exists(filepath):
             print(f"  Skipping Q{i} (File exists: {filename})")
             continue
             
        content = generate_markdown(client, i, q_text, template_content)
        
        if content:
            with open(filepath, 'w', encoding='utf-8') as f:
                f.write(content)
            print(f"  Saved to {filename}")
            time.sleep(0) # Rate limit politeness
        else:
            print(f"  Failed to generate Q{i}")

if __name__ == "__main__":
    main()
