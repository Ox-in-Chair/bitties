# Fix readonly input issues in transaction_form.html v1.2

with open('app/templates/transaction_form.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Remove readonly from BTC to Purchase field
content = content.replace(
    '<input type="number" id="btcAmount" class="form-control" step="0.00000001" required readonly>',
    '<input type="number" id="btcAmount" class="form-control" step="0.00000001" required>'
)

# Fix 2: Initialize simPrice on page load
init_fix = '''document.getElementById('pin1').focus();'''
if init_fix in content:
    content = content.replace(init_fix, '''document.getElementById('pin1').focus();

// Initialize simulation price
window.addEventListener('load', () => {
    setTimeout(() => {
        if (currentBTCPrice > 0) {
            document.getElementById('simPrice').value = currentBTCPrice.toFixed(2);
        }
    }, 1000);
});''')

# Fix 3: Update Est. BTC calculation when price loads
price_update = '''document.getElementById('btcPriceInput').value = currentBTCPrice.toFixed(2);'''
if price_update in content:
    content = content.replace(price_update, '''document.getElementById('btcPriceInput').value = currentBTCPrice.toFixed(2);
        
        // Update Est. BTC to Buy
        if (availableFunds > 0) {
            const estBTC = availableFunds / currentBTCPrice;
            document.getElementById('est-btc').textContent = estBTC.toFixed(8);
        }''')

# Fix 4: Update simulate function to update price
simulate_fix = '''document.getElementById('simPrice').value = price.toFixed(2);'''
if simulate_fix in content:
    content = content.replace(
        'const price = currentBTCPrice || 0;',
        'const price = currentBTCPrice || parseFloat(document.getElementById("btcPriceInput").value) || 0;'
    )

# Write updated file (Version: 1.2)
with open('app/templates/transaction_form.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Fixed input field issues in transaction form")
print("📝 Version: transaction_form.html v1.2")
print("\nFixed:")
print("- BTC to Purchase field now editable")
print("- Est. BTC to Buy auto-calculates")
print("- Simulation BTC Price shows current price")
print("\nRestart app to see changes!")