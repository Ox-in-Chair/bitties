# Fix missing json import in main.py

with open('app/main.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Check if json is imported
if 'import json' not in content:
    # Find the first import statement
    import_pos = content.find('from flask import')
    if import_pos != -1:
        # Find the end of that line
        end_of_line = content.find('\n', import_pos)
        # Add json import after the flask imports
        content = content[:end_of_line + 1] + 'import json\n' + content[end_of_line + 1:]
        
        # Save the fixed file
        with open('app/main.py', 'w', encoding='utf-8') as f:
            f.write(content)
        
        print("✅ Fixed: Added 'import json' to main.py")
    else:
        print("❌ Could not find import section")
else:
    print("✅ JSON import already exists")

print("\nRestart your app - the error should be fixed!")