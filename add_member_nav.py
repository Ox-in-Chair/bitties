# Add member management to navigation

with open('app/templates/base.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the navigation section and add Members button
if 'href="/members/manage"' not in content:
    # Find Record Purchase button
    purchase_pos = content.find('Record Purchase</a>')
    if purchase_pos != -1:
        insert_pos = content.find('</a>', purchase_pos) + 4
        new_nav = '''
                <a href="/members/manage" class="btn btn-primary" style="margin-left: 10px;">Members</a>'''
        content = content[:insert_pos] + new_nav + content[insert_pos:]
        
        with open('app/templates/base.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ Added Members button to navigation")
        print("📝 Version: base.html v1.1")
    else:
        print("❌ Could not find navigation section")
else:
    print("✅ Members link already exists")