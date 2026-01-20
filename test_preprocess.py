import re

from main import preprocess_content

# Test Data
valid_content = """
# Question
Question text

## Options
A) Valid 1
B) Valid 2

---
# Solution
"""

invalid_content = """
# Question
Question text

## Options
A) N/A
B) N/A

---
# Solution
"""

mixed_content = """
# Question
Question text

## Options
A) Real Option
B) N/A

---
# Solution
"""

# Testing
print("Testing Valid Content:")
res_valid = preprocess_content(valid_content)
if "## Options" in res_valid:
    print("PASS: Options preserved")
else:
    print("FAIL: Options removed mistakenly")
    print(res_valid)

print("\nTesting Invalid Content:")
res_invalid = preprocess_content(invalid_content)
if "## Options" not in res_invalid and "N/A" not in res_invalid:
    print("PASS: Options removed")
    # print(res_invalid)
else:
    print("FAIL: Options NOT removed")
    print(res_invalid)

print("\nTesting Mixed Content:")
res_mixed = preprocess_content(mixed_content)
if "## Options" not in res_mixed:
    print("PASS: Mixed Options removed")
else:
    print("FAIL: Mixed Options NOT removed")

