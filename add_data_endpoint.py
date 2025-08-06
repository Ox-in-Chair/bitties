import json

# Add this route to app/main.py after the existing routes

route_code = '''
@app.route('/api/fund/summary')
def api_fund_summary():
    """Get fund summary from historical data"""
    try:
        with open('data/fund_summary.json', 'r') as f:
            summary = json.load(f)
        return jsonify(summary)
    except FileNotFoundError:
        return jsonify({'error': 'Historical data not found'}), 404

@app.route('/api/fund/history')
def api_fund_history():
    """Get full historical data"""
    try:
        with open('data/historical_data.json', 'r') as f:
            history = json.load(f)
        return jsonify(history)
    except FileNotFoundError:
        return jsonify({'error': 'Historical data not found'}), 404
'''

# Read current main.py
with open('app/main.py', 'r') as f:
    content = f.read()

# Find where to insert (after the last route but before error handlers)
insert_position = content.rfind('@app.route')
if insert_position != -1:
    # Find the end of that route
    next_decorator = content.find('@app.errorhandler', insert_position)
    if next_decorator != -1:
        # Insert before error handlers
        new_content = content[:next_decorator] + route_code + '\n' + content[next_decorator:]
    else:
        # Just append
        new_content = content + '\n' + route_code
    
    # Backup and write
    import shutil
    shutil.copy('app/main.py', 'app/main_backup2.py')
    
    with open('app/main.py', 'w') as f:
        f.write(new_content)
    
    print("✅ API endpoints added to main.py")
else:
    print("❌ Could not find insertion point in main.py")
    print("Add these routes manually to app/main.py:")
    print(route_code)