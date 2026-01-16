import os
import re
from bs4 import BeautifulSoup

# Configuration
HTML_FILE = "database/drs/_question_list.html"
OUTPUT_DIR = "database/drs"

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

def sanitize_filename(text):
    # Same logic as the original parser
    text = re.sub(r'[^\w\s-]', '', text).strip().lower()
    text = re.sub(r'[-\s]+', '_', text)
    return text[:50]  # Limit length

def verify():
    questions = parse_questions(HTML_FILE)
    print(f"Total questions in HTML: {len(questions)}")
    
    missing_count = 0
    existing_files = set(os.listdir(OUTPUT_DIR))
    
    # We need to check if the *expected* filename exists.
    # Note: The problem is that multiple questions might map to the same filename.
    # So we need to track if a filename is "claimed" by an earlier question.
    
    claimed_filenames = {}
    
    print("\n--- Missing / Colliding Questions ---")
    
    for i, q_text in questions:
        filename = sanitize_filename(q_text) + ".md"
        
        if filename in claimed_filenames:
            prev_id = claimed_filenames[filename]
            print(f"[MISSING] Q{i} collides with Q{prev_id} on '{filename}'")
            print(f"    Q{i}: {q_text[:60]}...")
            missing_count += 1
        elif filename not in existing_files:
             # This might happen if I deleted files or if generation failed for other reasons
            print(f"[MISSING] Q{i} file not found: '{filename}'")
            missing_count += 1
        else:
            claimed_filenames[filename] = i
            
    print(f"\nTotal missing/colliding questions: {missing_count}")


if __name__ == "__main__":
    print(f"Checking directory: {os.path.abspath(OUTPUT_DIR)}")
    if not os.path.exists(OUTPUT_DIR):
        print(f"ERROR: Directory not found: {os.path.abspath(OUTPUT_DIR)}")
    else:
        verify()
