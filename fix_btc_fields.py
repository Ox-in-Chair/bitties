# Fix BTC field issues in transaction_form.html v1.3

with open('app/templates/transaction_form.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Make simulation BTC Price field editable and update simulate function
content = content.replace(
    '<input type="number" id="simPrice" class="form-control" readonly>',
    '<input type="number" id="simPrice" class="form-control" step="0.01" onkeyup="simulate()">'
)

# Fix 2: Update simulate function to use manual price if entered
old_simulate = '''function simulate() {
    const amount = parseFloat(document.getElementById('simAmount').value) || 0;
    const price = currentBTCPrice || parseFloat(document.getElementById("btcPriceInput").value) || 0;
    document.getElementById('simPrice').value = price.toFixed(2);'''

new_simulate = '''function simulate() {
    const amount = parseFloat(document.getElementById('simAmount').value) || 0;
    let price = parseFloat(document.getElementById('simPrice').value) || 0;
    if (price === 0) {
        price = currentBTCPrice || parseFloat(document.getElementById("btcPriceInput").value) || 0;
        document.getElementById('simPrice').value = price.toFixed(2);
    }'''

content = content.replace(old_simulate, new_simulate)

# Fix 3: Add Total Holdings field after BTC to Purchase
btc_purchase_section = '''                        <div>
                            <label style="display: block; margin-bottom: 0.5rem;">BTC to Purchase</label>
                            <input type="number" id="btcAmount" class="form-control" step="0.00000001" required>
                        </div>'''

holdings_field = '''                        <div>
                            <label style="display: block; margin-bottom: 0.5rem;">BTC to Purchase</label>
                            <input type="number" id="btcAmount" class="form-control" step="0.00000001" required>
                        </div>
                    </div>
                    
                    <div style="margin-bottom: 1rem;">
                        <label style="display: block; margin-bottom: 0.5rem;">New Total BTC Holdings (after purchase)</label>
                        <input type="number" id="totalHoldings" class="form-control" step="0.00000001" required placeholder="Enter total holdings after this purchase">'''

content = content.replace(btc_purchase_section + '\n                    </div>', holdings_field)

# Fix 4: Update recordPurchase to include total holdings
old_purchase_data = '''    const purchaseData = {
        date: document.getElementById('purchaseDate').value,
        btc_price_zar: parseFloat(document.getElementById('btcPriceInput').value),
        amount_zar: parseFloat(document.getElementById('amountZAR').value),
        btc_amount: parseFloat(document.getElementById('btcAmount').value),
        notes: document.getElementById('notes').value
    };'''

new_purchase_data = '''    const purchaseData = {
        date: document.getElementById('purchaseDate').value,
        btc_price_zar: parseFloat(document.getElementById('btcPriceInput').value),
        amount_zar: parseFloat(document.getElementById('amountZAR').value),
        btc_amount: parseFloat(document.getElementById('btcAmount').value),
        total_holdings: parseFloat(document.getElementById('totalHoldings').value),
        notes: document.getElementById('notes').value
    };'''

content = content.replace(old_purchase_data, new_purchase_data)

# Fix 5: Auto-populate suggested total holdings
calc_btc_update = '''        document.getElementById('btcAmount').value = btcAmount.toFixed(8);
        document.getElementById('est-btc').textContent = btcAmount.toFixed(8);'''

calc_btc_new = '''        document.getElementById('btcAmount').value = btcAmount.toFixed(8);
        document.getElementById('est-btc').textContent = btcAmount.toFixed(8);
        
        // Suggest new total holdings
        const currentHoldings = parseFloat(document.getElementById('current-btc').textContent) || 0;
        const suggestedTotal = currentHoldings + btcAmount;
        document.getElementById('totalHoldings').value = suggestedTotal.toFixed(8);'''

content = content.replace(calc_btc_update, calc_btc_new)

# Write updated file (Version: 1.3)
with open('app/templates/transaction_form.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Fixed BTC fields in transaction form")
print("📝 Version: transaction_form.html v1.3")
print("\nFixed:")
print("- Quick Calculator BTC Price now editable")
print("- Added Total BTC Holdings field for manual input")
print("- Auto-suggests new total (current + purchase)")
print("\nRestart app to test!")