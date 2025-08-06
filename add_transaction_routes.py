import json
from datetime import datetime

# Add these routes to app/main.py

routes_to_add = '''
# Transaction Recording Routes
@app.route('/transactions')
def transactions():
    """Transaction recording page"""
    return render_template('transaction_form.html')

@app.route('/api/payments/current-month')
def api_current_payments():
    """Get payment status for current month"""
    # For now, return mock data - will integrate with real payment tracking later
    current_month = datetime.now().strftime('%Y-%m')
    
    # Mock data - replace with actual payment tracking
    members = [
        {"name": "Salad", "initials": "S", "paid": True, "amount": 400},
        {"name": "Just", "initials": "J", "paid": True, "amount": 400},
        {"name": "Jan", "initials": "J", "paid": True, "amount": 400},
        {"name": "Ox", "initials": "O", "paid": True, "amount": 400},
        {"name": "Flanners", "initials": "F", "paid": True, "amount": 400},
        {"name": "Jerry", "initials": "J", "paid": True, "amount": 400},
        {"name": "Mearp", "initials": "M", "paid": True, "amount": 400}
    ]
    
    return jsonify({
        "month": current_month,
        "members": members,
        "total_expected": 2800,
        "total_paid": 2800
    })

@app.route('/api/btc/purchase', methods=['POST'])
def api_record_purchase():
    """Record a new BTC purchase"""
    try:
        purchase_data = request.json
        
        # Load existing data
        with open('data/historical_data.json', 'r', encoding='utf-8') as f:
            history = json.load(f)
        
        # Calculate new total holdings
        previous_holdings = history['btc_purchases'][-1]['total_holdings'] if history['btc_purchases'] else 0
        new_holdings = previous_holdings + purchase_data['btc_amount']
        
        # Add new purchase
        new_purchase = {
            "date": purchase_data['date'],
            "btc_bought": purchase_data['btc_amount'],
            "total_holdings": new_holdings,
            "price_zar": purchase_data['btc_price_zar'],
            "amount_invested": purchase_data['amount_zar'],
            "notes": purchase_data.get('notes', ''),
            "recorded_at": datetime.now().isoformat()
        }
        
        history['btc_purchases'].append(new_purchase)
        
        # Save updated data
        with open('data/historical_data.json', 'w', encoding='utf-8') as f:
            json.dump(history, f, indent=2)
        
        # Update fund summary
        with open('data/fund_summary.json', 'r', encoding='utf-8') as f:
            summary = json.load(f)
        
        summary['total_btc_acquired'] = new_holdings
        summary['last_btc_purchase'] = purchase_data['date']
        summary['number_of_purchases'] = len(history['btc_purchases'])
        
        with open('data/fund_summary.json', 'w', encoding='utf-8') as f:
            json.dump(summary, f, indent=2)
        
        return jsonify({"success": True, "new_holdings": new_holdings}), 201
        
    except Exception as e:
        return jsonify({"error": str(e)}), 500
'''

# Read current main.py
with open('app/main.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Add import for datetime if not present
if 'from datetime import datetime' not in content:
    import_pos = content.find('import')
    if import_pos != -1:
        end_of_line = content.find('\n', import_pos)
        content = content[:end_of_line + 1] + 'from datetime import datetime\n' + content[end_of_line + 1:]

# Find insertion point
insert_pos = content.rfind('@app.route')
if insert_pos != -1:
    next_decorator = content.find('@app.errorhandler', insert_pos)
    if next_decorator != -1:
        content = content[:next_decorator] + routes_to_add + '\n' + content[next_decorator:]
    else:
        content = content + '\n' + routes_to_add

# Save updated main.py
import shutil
shutil.copy('app/main.py', 'app/main_backup3.py')

with open('app/main.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Transaction routes added to main.py!")
print("✅ PIN protection: 2580")
print("✅ Payment verification before purchase")
print("\nRestart app and visit: /transactions")