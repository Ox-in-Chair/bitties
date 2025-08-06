# Minimal edit to add simulation feature to transaction_form.html

with open('app/templates/transaction_form.html', 'r', encoding='utf-8') as f:
    content = f.read()

# Find where to insert simulation section (after payment status card)
insert_marker = '<!-- Purchase Form -->'
if insert_marker in content:
    simulation_html = '''
            <!-- BTC Simulation Tool -->
            <div class="card" style="margin-bottom: 2rem;">
                <h2 class="card-title">Quick BTC Calculator</h2>
                <div class="grid grid-3" style="gap: 1rem;">
                    <div>
                        <label style="display: block; margin-bottom: 0.5rem;">Amount (ZAR)</label>
                        <input type="number" id="simAmount" class="form-control" placeholder="1000" onkeyup="simulate()">
                    </div>
                    <div>
                        <label style="display: block; margin-bottom: 0.5rem;">BTC Price</label>
                        <input type="number" id="simPrice" class="form-control" readonly>
                    </div>
                    <div>
                        <label style="display: block; margin-bottom: 0.5rem;">BTC You'd Get</label>
                        <input type="text" id="simResult" class="form-control" readonly style="font-weight: 600;">
                    </div>
                </div>
            </div>

            '''
    
    # Insert before Purchase Form
    content = content.replace(insert_marker, simulation_html + insert_marker)
    
    # Add simulate function to script section
    script_insert = 'calculateBTC();'
    if script_insert in content:
        simulate_function = '''
        
// Quick simulation
function simulate() {
    const amount = parseFloat(document.getElementById('simAmount').value) || 0;
    const price = currentBTCPrice || 0;
    document.getElementById('simPrice').value = price.toFixed(2);
    if (amount > 0 && price > 0) {
        const btc = amount / price;
        document.getElementById('simResult').value = btc.toFixed(8) + ' BTC';
    } else {
        document.getElementById('simResult').value = '0.00000000 BTC';
    }
}'''
        content = content.replace(script_insert, script_insert + simulate_function)
    
    # Write updated file (Version: 1.1)
    with open('app/templates/transaction_form.html', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print("✅ Added BTC simulation calculator to transaction form")
    print("📝 Version: transaction_form.html v1.1")
else:
    print("❌ Could not find insertion marker")