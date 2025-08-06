# Add member management routes to main.py

routes_to_add = '''
# Member Management Routes
@app.route('/members/manage')
def members_manage():
    """Member management page"""
    return render_template('member_management.html')

@app.route('/api/members/add', methods=['POST'])
def api_add_member():
    """Add new member with entry fee"""
    try:
        data = request.json
        
        # Load existing data
        with open('data/historical_data.json', 'r', encoding='utf-8') as f:
            history = json.load(f)
        
        # Generate new member ID
        max_id = max([m['id'] for m in history['members']] + [0])
        new_member = {
            'id': max_id + 1,
            'name': data['name'],
            'joined_date': data['join_date'],
            'leave_date': None,
            'status': 'active',
            'role': 'member'
        }
        
        history['members'].append(new_member)
        
        # Record entry fee as contribution
        entry_contribution = {
            'date': data['join_date'],
            'member_id': new_member['id'],
            'member_name': data['name'],
            'amount_zar': data['entry_fee'],
            'type': 'entry_fee'
        }
        
        history['contributions'].append(entry_contribution)
        
        # Save updated data
        with open('data/historical_data.json', 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=2)
        
        # Update summary
        with open('data/fund_summary.json', 'r', encoding='utf-8') as f:
            summary = json.load(f)
        
        summary['active_members'] = len([m for m in history['members'] if m['status'] == 'active'])
        summary['member_contributions'][data['name']] = data['entry_fee']
        summary['total_contributions_zar'] += data['entry_fee']
        
        with open('data/fund_summary.json', 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2)
        
        return jsonify({'success': True, 'member': new_member}), 201
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/members/<int:member_id>/remove', methods=['POST'])
def api_remove_member(member_id):
    """Remove member with exit settlement"""
    try:
        data = request.json
        
        # Load existing data
        with open('data/historical_data.json', 'r', encoding='utf-8') as f:
            history = json.load(f)
        
        # Find member
        member = next((m for m in history['members'] if m['id'] == member_id), None)
        if not member:
            return jsonify({'error': 'Member not found'}), 404
        
        # Update member status
        member['status'] = 'left'
        member['leave_date'] = datetime.now().strftime('%Y-%m-%d')
        
        # Record BTC withdrawal
        btc_withdrawal = {
            'date': member['leave_date'],
            'btc_bought': 0,
            'total_holdings': history['btc_purchases'][-1]['total_holdings'] - data['exit_btc'],
            'price_zar': data['btc_price'],
            'type': 'withdrawal',
            'member': member['name'],
            'amount_withdrawn': data['exit_btc']
        }
        
        history['btc_purchases'].append(btc_withdrawal)
        
        # Save updated data
        with open('data/historical_data.json', 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=2)
        
        # Update summary
        with open('data/fund_summary.json', 'r', encoding='utf-8') as f:
            summary = json.load(f)
        
        summary['active_members'] = len([m for m in history['members'] if m['status'] == 'active'])
        summary['total_btc_acquired'] = btc_withdrawal['total_holdings']
        
        with open('data/fund_summary.json', 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2)
        
        return jsonify({'success': True, 'new_holdings': btc_withdrawal['total_holdings']}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500
'''

# Read current main.py
with open('app/main.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find insertion point
insert_pos = content.rfind('@app.route')
if insert_pos != -1:
    next_decorator = content.find('@app.errorhandler', insert_pos)
    if next_decorator != -1:
        content = content[:next_decorator] + routes_to_add + '\n' + content[next_decorator:]
    else:
        content = content + '\n' + routes_to_add

# Save updated main.py (v1.4)
with open('app/main.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Added member management API routes")
print("📝 Version: main.py v1.4")
print("Routes added:")
print("- /members/manage - UI page")
print("- /api/members/add - Add with entry fee")
print("- /api/members/<id>/remove - Remove with settlement")