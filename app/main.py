# Save this as: app/main.py (replace the existing one)

"""Bitties - Main Application Module"""
from flask import Flask, render_template, jsonify, request
import json
from datetime import datetime
from flask_cors import CORS
import os
import sys

# Add parent directory to path
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from app.services.data_manager import DataManager
from app.api.btc_data import get_current_btc_price, get_btc_history

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'dev-key-change-in-production')
CORS(app)

# Initialize data manager
data_manager = DataManager()

# Routes
@app.route('/')
def index():
    """Home page"""
    return render_template('index.html')

@app.route('/dashboard')
def dashboard():
    """Main dashboard"""
    return render_template('dashboard.html')

@app.route('/test')
def test():
    return render_template('test.html')

@app.route('/members')
def members():
    """Members page"""
    return render_template('members.html')

# API Routes
@app.route('/api/status')
def api_status():
    """API status endpoint"""
    return jsonify({
        'status': 'online',
        'version': '1.0.0'
    })

@app.route('/api/members', methods=['GET', 'POST'])
def api_members():
    """Get all members or add new member"""
    if request.method == 'POST':
        member_data = request.json
        new_member = data_manager.add_member(member_data)
        return jsonify(new_member), 201
    
    members = data_manager.get_members()
    return jsonify(members)

@app.route('/api/members/<member_id>')
def api_member(member_id):
    """Get specific member"""
    member = data_manager.get_member(member_id)
    if member:
        return jsonify(member)
    return jsonify({'error': 'Member not found'}), 404

@app.route('/api/transactions', methods=['GET', 'POST'])
def api_transactions():
    """Get all transactions or add new transaction"""
    if request.method == 'POST':
        transaction_data = request.json
        
        # Get current BTC price if not provided
        if 'btc_price_zar' not in transaction_data:
            prices = get_current_btc_price()
            transaction_data['btc_price_zar'] = prices['zar']
            transaction_data['btc_price_usd'] = prices['usd']
        
        new_transaction = data_manager.add_transaction(transaction_data)
        return jsonify(new_transaction), 201
    
    transactions = data_manager.get_transactions()
    return jsonify(transactions)

@app.route('/api/portfolio')
def api_portfolio():
    """Get portfolio summary"""
    summary = data_manager.get_portfolio_summary()
    
    # Add current prices
    prices = get_current_btc_price()
    summary['current_btc_price_zar'] = prices['zar']
    summary['current_btc_price_usd'] = prices['usd']
    summary['current_value_zar'] = summary['total_btc'] * prices['zar']
    summary['current_value_usd'] = summary['total_btc'] * prices['usd']
    summary['profit_loss_zar'] = summary['current_value_zar'] - summary['total_invested_zar']
    summary['profit_loss_percentage'] = (
        (summary['profit_loss_zar'] / summary['total_invested_zar'] * 100) 
        if summary['total_invested_zar'] > 0 else 0
    )
    
    return jsonify(summary)

@app.route('/api/btc/price')
def api_btc_price():
    """Get current BTC price"""
    price_data = get_current_btc_price()
    return jsonify(price_data)

@app.route('/api/btc/history')
def api_btc_history():
    """Get BTC price history"""
    days = request.args.get('days', 30, type=int)
    history = get_btc_history(days)
    return jsonify(history)

@app.errorhandler(404)
def not_found(error):
    return jsonify({'error': 'Not found'}), 404

@app.errorhandler(500)
def internal_error(error):
    return jsonify({'error': 'Internal server error'}), 500

if __name__ == '__main__':
    app.run(debug=True)@app.route('/minimal') 
def minimal(): 
    return render_template('minimal.html') 
 
# @app.route('/minimal') 
def minimal(): 
    return render_template('minimal.html') 
 
# @app.route('/minimal') 
def minimal(): 
    return render_template('minimal.html') 
 
 
@app.route('/dashboard_original') 
def dashboard_original(): 
    return render_template('dashboard_original.html') 


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
        
        # Use manual total holdings from form
        new_holdings = purchase_data.get('total_holdings')
        if not new_holdings:
            # Fallback: calculate if not provided
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


@app.route('/corrections')
def corrections():
    """Data corrections page"""
    return render_template('corrections.html')

@app.route('/config')
def config():
    """System configuration page"""
    return render_template('config.html')
