# Check if routes were added properly and fix if needed

with open('app/main.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Check if corrections route exists
if '@app.route(\'/corrections\')' not in content:
    print("❌ Corrections route missing - adding now")
    
    # Find the last route before error handlers
    last_route_pos = content.rfind('@app.route')
    error_handler_pos = content.find('@app.errorhandler', last_route_pos)
    
    routes_to_add = '''
@app.route('/corrections')
def corrections():
    """Data corrections page"""
    return render_template('corrections.html')
'''
    
    if error_handler_pos != -1:
        # Insert before error handlers
        content = content[:error_handler_pos] + routes_to_add + content[error_handler_pos:]
    else:
        # Just append
        content = content + '\n' + routes_to_add
    
    # Save fixed main.py
    with open('app/main.py', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Added missing corrections route")
else:
    print("✅ Corrections route already exists")

# Verify the template exists
import os
if not os.path.exists('app/templates/corrections.html'):
    print("❌ corrections.html template missing!")
else:
    print("✅ corrections.html template exists")