# Add corrections routes and update navigation

import shutil

# First, add routes to main.py
routes_to_add = '''
# Data Corrections Routes
@app.route('/corrections')
def corrections():
    """Data corrections page"""
    return render_template('corrections.html')

@app.route('/api/corrections/holdings', methods=['POST'])
def api_correct_holdings():
    """Manually correct total BTC holdings"""
    try:
        data = request.json
        new_holdings = data['new_holdings']
        
        # Update fund summary
        with open('data/fund_summary.json', 'r', encoding='utf-8') as f:
            summary = json.load(f)
        
        summary['total_btc_acquired'] = new_holdings
        
        with open('data/fund_summary.json', 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2)
        
        # Add correction entry to history
        with open('data/historical_data.json', 'r', encoding='utf-8') as f:
            history = json.load(f)
        
        correction_entry = {
            "date": datetime.now().strftime('%Y-%m-%d'),
            "btc_bought": 0,
            "total_holdings": new_holdings,
            "price_zar": 0,
            "type": "manual_correction",
            "notes": f"Manual correction to {new_holdings} BTC"
        }
        
        history['btc_purchases'].append(correction_entry)
        
        with open('data/historical_data.json', 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=2)
        
        return jsonify({'success': True, 'new_holdings': new_holdings}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/corrections/delete-last', methods=['POST'])
def api_delete_last_purchase():
    """Delete the last purchase entry"""
    try:
        # Load and modify history
        with open('data/historical_data.json', 'r', encoding='utf-8') as f:
            history = json.load(f)
        
        if not history['btc_purchases']:
            return jsonify({'error': 'No purchases to delete'}), 400
        
        # Remove last purchase
        deleted = history['btc_purchases'].pop()
        
        # Update holdings to previous value
        if history['btc_purchases']:
            new_holdings = history['btc_purchases'][-1]['total_holdings']
        else:
            new_holdings = 0
        
        with open('data/historical_data.json', 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=2)
        
        # Update summary
        with open('data/fund_summary.json', 'r', encoding='utf-8') as f:
            summary = json.load(f)
        
        summary['total_btc_acquired'] = new_holdings
        summary['number_of_purchases'] = len(history['btc_purchases'])
        
        with open('data/fund_summary.json', 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2)
        
        return jsonify({'success': True, 'deleted': deleted}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
'''

# Read and update main.py
with open('app/main.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Insert routes
insert_pos = content.rfind('@app.route')
if insert_pos != -1:
    next_decorator = content.find('@app.errorhandler', insert_pos)
    if next_decorator != -1:
        content = content[:next_decorator] + routes_to_add + '\n' + content[next_decorator:]

# Save main.py v1.5
with open('app/main.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Added corrections API routes")
print("📝 Version: main.py v1.5")

# Now update navigation - rename Members to Member Setup and add Corrections
with open('app/templates/base.html', 'r', encoding='utf-8') as f:
    nav_content = f.read()

# Update Members text
nav_content = nav_content.replace('>Members</a>', '>Member Setup</a>')

# Add Corrections button
if 'href="/corrections"' not in nav_content:
    members_pos = nav_content.find('Member Setup</a>')
    if members_pos != -1:
        insert_pos = nav_content.find('</a>', members_pos) + 4
        new_nav = '''
                <a href="/corrections" class="btn btn-primary" style="margin-left: 10px; background: var(--accent-red);">Corrections</a>'''
        nav_content = nav_content[:insert_pos] + new_nav + nav_content[insert_pos:]

# Save base.html v1.2
with open('app/templates/base.html', 'w', encoding='utf-8') as f:
    f.write(nav_content)

print("✅ Updated navigation")
print("📝 Version: base.html v1.2")
print("- Renamed 'Members' to 'Member Setup'")
print("- Added 'Corrections' button")