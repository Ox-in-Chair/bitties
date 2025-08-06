# Update base.html to include transaction link
import re

with open('app/templates/base.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the Dashboard button and add Transaction button after it
if 'href="/transactions"' not in content:
    # Find the dashboard button
    dashboard_match = re.search(r'(<a href="/dashboard"[^>]*>Dashboard</a>)', content)
    if dashboard_match:
        # Add transaction button after dashboard
        new_nav = dashboard_match.group(0) + '''
                <a href="/transactions" class="btn btn-primary" style="margin-left: 10px;">Record Purchase</a>'''
        content = content.replace(dashboard_match.group(0), new_nav)
        
        with open('app/templates/base.html', 'w', encoding='utf-8') as f:
            f.write(content)
        print("✅ Navigation updated with Record Purchase button")
    else:
        print("❌ Could not find navigation section")
else:
    print("✅ Transaction link already exists")