import os

DIR = "/home/basta/Projects/DIT-exam/database/drs"

def fix_file(path):
    with open(path, "r") as f:
        content = f.read()

    if not content.startswith("---"):
        return False

    # Find the start of the Question section
    q_idx = content.find("\n# Question")
    if q_idx == -1:
        return False

    # Check the segment between the start and the Question
    # content[3:q_idx] covers everything after the first `---` until `# Question`
    header_segment = content[3:q_idx]

    # If there is no closing `---` in this segment, it's malformed
    if "\n---" not in header_segment:
        print(f"Fixing {os.path.basename(path)}")
        # Construct new content:
        # Keep header segment, add `---`, then the question part
        # content[:q_idx] is everything up to the newline before `# Question`
        # We append `\n---\n` and then the rest starting from that newline
        # Actually, `q_idx` points to `\n` in `\n# Question`
        
        # New split:
        # Part1: content[:q_idx] (Metadata)
        # Part2: content[q_idx:] (The `\n# Question...`)
        
        # We want to insert `\n---` between them.
        # But Part1 might not end with a newline if we are not careful, 
        # though `q_idx` finds `\n#`.
        
        new_content = content[:q_idx] + "\n---" + content[q_idx:]
        
        with open(path, "w") as f:
            f.write(new_content)
        return True
    return False

count = 0
files = [f for f in os.listdir(DIR) if f.endswith(".md")]
for f in files:
    if fix_file(os.path.join(DIR, f)):
        count += 1

print(f"Fixed {count} files.")
