# Update purchase API to use manual total holdings v1.3

with open('app/main.py', 'r', encoding='utf-8') as f:
    content = f.read()

# Find and update the purchase recording logic
old_holdings_calc = '''        # Calculate new total holdings
        previous_holdings = history['btc_purchases'][-1]['total_holdings'] if history['btc_purchases'] else 0
        new_holdings = previous_holdings + purchase_data['btc_amount']'''

new_holdings_calc = '''        # Use manual total holdings from form
        new_holdings = purchase_data.get('total_holdings')
        if not new_holdings:
            # Fallback: calculate if not provided
            previous_holdings = history['btc_purchases'][-1]['total_holdings'] if history['btc_purchases'] else 0
            new_holdings = previous_holdings + purchase_data['btc_amount']'''

content = content.replace(old_holdings_calc, new_holdings_calc)

# Write updated file
with open('app/main.py', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Updated API to accept manual total holdings")
print("📝 Version: main.py v1.3")