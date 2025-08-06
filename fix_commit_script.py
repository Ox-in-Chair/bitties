# Fix the encoding issue in bitties_commit.py
import re

# Read the file
with open('bitties_commit.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Replace all file write operations to include encoding='utf-8'
content = content.replace(
    "with open('HANDOVER.md', 'w') as f:",
    "with open('HANDOVER.md', 'w', encoding='utf-8') as f:"
)
content = content.replace(
    "with open('README.md', 'w') as f:",
    "with open('README.md', 'w', encoding='utf-8') as f:"
)

# Also need to fix the file read operations
content = content.replace(
    "with open('data/fund_summary.json', 'r') as f:",
    "with open('data/fund_summary.json', 'r', encoding='utf-8') as f:"
)
content = content.replace(
    "with open('HANDOVER.md', 'r') as f:",
    "with open('HANDOVER.md', 'r', encoding='utf-8') as f:"
)
content = content.replace(
    "with open('README.md', 'r') as f:",
    "with open('README.md', 'r', encoding='utf-8') as f:"
)

# Write the fixed version
with open('bitties_commit.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Fixed encoding issues in bitties_commit.py")
print("You can now run: python bitties_commit.py \"your message\"")