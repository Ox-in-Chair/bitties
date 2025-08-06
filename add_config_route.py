# Add config route and update navigation

import os

# Add config route to main.py
with open('app/main.py', 'r', encoding='utf-8') as f:
    content = f.read()

if '@app.route(\'/config\')' not in content:
    # Find insertion point
    last_route = content.rfind('@app.route')
    error_pos = content.find('@app.errorhandler', last_route)
    
    config_route = '''
@app.route('/config')
def config():
    """System configuration page"""
    return render_template('config.html')
'''
    
    if error_pos != -1:
        content = content[:error_pos] + config_route + content[error_pos:]
    else:
        content = content + config_route
    
    with open('app/main.py', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Added config route to main.py")

# Update navigation - replace individual buttons with single Config button
with open('app/templates/base.html', 'r', encoding='utf-8') as f:
    nav_content = f.read()

# Remove old Member Setup and Corrections buttons, add Config
if '>Config</a>' not in nav_content:
    # Find and remove Member Setup button
    member_start = nav_content.find('<a href="/members/manage"')
    if member_start != -1:
        member_end = nav_content.find('</a>', member_start) + 4
        nav_content = nav_content[:member_start] + nav_content[member_end:]
    
    # Find and remove Corrections button
    corrections_start = nav_content.find('<a href="/corrections"')
    if corrections_start != -1:
        corrections_end = nav_content.find('</a>', corrections_start) + 4
        nav_content = nav_content[:corrections_start] + nav_content[corrections_end:]
    
    # Add Config button after Record Purchase
    purchase_pos = nav_content.find('Record Purchase</a>')
    if purchase_pos != -1:
        insert_pos = nav_content.find('</a>', purchase_pos) + 4
        config_btn = '''
                <a href="/config" class="btn btn-primary" style="margin-left: 10px; background: var(--text-muted);">Config</a>'''
        nav_content = nav_content[:insert_pos] + config_btn + nav_content[insert_pos:]
    
    with open('app/templates/base.html', 'w', encoding='utf-8') as f:
        f.write(nav_content)
    
    print("✅ Updated navigation - replaced multiple buttons with Config")
    print("📝 Version: base.html v1.3")

print("\n✅ Configuration complete!")
print("- Config page with 3 sub-tabs")
print("- Member Setup and Corrections now under Config")
print("- Single PIN protection for all config features")