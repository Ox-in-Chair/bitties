# Fix dashboard to show updated data after purchases

with open('app/templates/dashboard.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the total BTC display and make it dynamic
old_btc = '''            <div class="stat-card">
                <div class="stat-label">Total BTC</div>
                <div class="stat-value" id="total-btc">0.11107669</div>
            </div>'''

new_btc = '''            <div class="stat-card">
                <div class="stat-label">Total BTC</div>
                <div class="stat-value" id="total-btc">Loading...</div>
            </div>'''

content = content.replace(old_btc, new_btc)

# Find the loadFundData function and update it to refresh BTC holdings
old_load = '''        // Store fund data globally
        window.fundData = fundData;'''

new_load = '''        // Update displayed values
        document.getElementById('total-btc').textContent = fundData.total_btc_acquired.toFixed(8);
        
        // Store fund data globally
        window.fundData = fundData;'''

content = content.replace(old_load, new_load)

# Also update the hardcoded values in calculations
old_calc = '''        // Use real BTC amount from fund data
        const totalBTC = 0.11107669;
        const totalInvested = 99600;'''

new_calc = '''        // Use real BTC amount from fund data
        const totalBTC = window.fundData ? window.fundData.total_btc_acquired : 0;
        const totalInvested = window.fundData ? window.fundData.total_contributions_zar : 0;'''

content = content.replace(old_calc, new_calc)

# Save updated dashboard (v1.1)
with open('app/templates/dashboard.html', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ Fixed dashboard to show live data")
print("📝 Version: dashboard.html v1.1")
print("Dashboard will now update after purchases!")