# Fix BTC formatting issues in transaction_form.html v1.4

with open('app/templates/transaction_form.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Fix 1: Change all BTC input fields from type="number" to type="text" with pattern
# This prevents scientific notation (9e-8) display
content = content.replace(
    '<input type="number" id="btcAmount" class="form-control" step="0.00000001" required>',
    '<input type="text" id="btcAmount" class="form-control" pattern="[0-9]+\.?[0-9]*" required placeholder="0.00000000">'
)

content = content.replace(
    '<input type="number" id="totalHoldings" class="form-control" step="0.00000001" required placeholder="Enter total holdings after this purchase">',
    '<input type="text" id="totalHoldings" class="form-control" pattern="[0-9]+\.?[0-9]*" required placeholder="0.00000000">'
)

# Fix 2: Update calculateBTC to format properly
old_calc = '''function calculateBTC() {
    const amountZAR = parseFloat(document.getElementById('amountZAR').value) || 0;
    const btcPrice = parseFloat(document.getElementById('btcPriceInput').value) || currentBTCPrice;
    
    if (amountZAR > 0 && btcPrice > 0) {
        const btcAmount = amountZAR / btcPrice;
        document.getElementById('btcAmount').value = btcAmount.toFixed(8);
        document.getElementById('est-btc').textContent = btcAmount.toFixed(8);
        
        // Suggest new total holdings
        const currentHoldings = parseFloat(document.getElementById('current-btc').textContent) || 0;
        const suggestedTotal = currentHoldings + btcAmount;
        document.getElementById('totalHoldings').value = suggestedTotal.toFixed(8);
    }
}'''

new_calc = '''function calculateBTC() {
    const amountZAR = parseFloat(document.getElementById('amountZAR').value) || 0;
    const btcPrice = parseFloat(document.getElementById('btcPriceInput').value) || currentBTCPrice;
    
    if (amountZAR > 0 && btcPrice > 0) {
        const btcAmount = amountZAR / btcPrice;
        // Format without scientific notation
        document.getElementById('btcAmount').value = btcAmount.toFixed(8);
        document.getElementById('est-btc').textContent = btcAmount.toFixed(8);
        
        // Suggest new total holdings
        const currentHoldings = parseFloat(document.getElementById('current-btc').textContent) || 0;
        const suggestedTotal = currentHoldings + btcAmount;
        document.getElementById('totalHoldings').value = suggestedTotal.toFixed(8);
    }
}

// Add reverse calculation when BTC amount is manually entered
document.getElementById('btcAmount').addEventListener('input', function() {
    const btcAmount = parseFloat(this.value) || 0;
    const btcPrice = parseFloat(document.getElementById('btcPriceInput').value) || currentBTCPrice;
    
    if (btcAmount > 0 && btcPrice > 0) {
        const amountZAR = btcAmount * btcPrice;
        document.getElementById('amountZAR').value = amountZAR.toFixed(2);
        
        // Update total holdings
        const currentHoldings = parseFloat(document.getElementById('current-btc').textContent) || 0;
        const suggestedTotal = currentHoldings + btcAmount;
        document.getElementById('totalHoldings').value = suggestedTotal.toFixed(8);
    }
});'''

content = content.replace(old_calc, new_calc)

# Fix 3: Update simulate function to auto-calculate
old_simulate_end = '''    if (amount > 0 && price > 0) {
        const btc = amount / price;
        document.getElementById('simResult').value = btc.toFixed(8) + ' BTC';
    } else {
        document.getElementById('simResult').value = '0.00000000 BTC';
    }
}'''

new_simulate_end = '''    if (amount > 0 && price > 0) {
        const btc = amount / price;
        document.getElementById('simResult').value = btc.toFixed(8) + ' BTC';
    } else {
        document.getElementById('simResult').value = '0.00000000 BTC';
    }
}

// Also trigger simulation when price changes
document.getElementById('simPrice').addEventListener('input', simulate);'''

content = content.replace(old_simulate_end, new_simulate_end)

# Fix 4: Add edit button after successful submission (in the success alert section)
old_alert = '''        if (response.ok) {
            alert('Purchase recorded successfully!');
            window.location.href = '/dashboard';
        }'''

new_alert = '''        if (response.ok) {
            const result = await response.json();
            if (confirm('Purchase recorded successfully! New holdings: ' + result.new_holdings.toFixed(8) + ' BTC\\n\\nReturn to dashboard?')) {
                window.location.href = '/dashboard';
            } else {
                // Stay on form for potential edits
                loadFundStatus();
            }
        }'''

content = content.replace(old_alert, new_alert)

# Write updated file (Version: 1.4)
with open('app/templates/transaction_form.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Fixed BTC formatting and calculations")
print("📝 Version: transaction_form.html v1.4")
print("\nFixed:")
print("- BTC fields now use text input (no more 9e-8)")
print("- Can type values directly (not just arrows)")
print("- Auto-calculates when you change any field")
print("- Confirmation dialog after submission")
print("- Option to stay on form for edits")