# Create corrections interface for fixing data errors

corrections_template = '''{% extends "base.html" %}
{% block title %}Bitties - Data Corrections{% endblock %}
{% block content %}
<section class="section">
    <div class="container">
        <h1 style="color: var(--primary-blue); margin-bottom: 2rem;">Data Corrections</h1>
        
        <!-- PIN Protection Modal -->
        <div id="pinModal" class="modal active">
            <div class="modal-content" style="max-width: 400px;">
                <h2 style="text-align: center; margin-bottom: 1.5rem;">Admin Access Required</h2>
                <p style="text-align: center; color: var(--accent-red); margin-bottom: 1rem;">
                    ⚠️ Warning: This section allows direct data modification
                </p>
                <div style="display: flex; justify-content: center; gap: 10px; margin-bottom: 1.5rem;">
                    <input type="password" id="pin1" maxlength="1" style="width: 50px; height: 50px; text-align: center; font-size: 24px;" class="form-control">
                    <input type="password" id="pin2" maxlength="1" style="width: 50px; height: 50px; text-align: center; font-size: 24px;" class="form-control">
                    <input type="password" id="pin3" maxlength="1" style="width: 50px; height: 50px; text-align: center; font-size: 24px;" class="form-control">
                    <input type="password" id="pin4" maxlength="1" style="width: 50px; height: 50px; text-align: center; font-size: 24px;" class="form-control">
                </div>
                <button onclick="checkPIN()" class="btn btn-primary" style="width: 100%;">Submit</button>
            </div>
        </div>

        <!-- Main Content -->
        <div id="mainContent" style="display: none;">
            
            <!-- Manual Holdings Adjustment -->
            <div class="card" style="margin-bottom: 2rem;">
                <h2 class="card-title">Manual Holdings Adjustment</h2>
                <p style="color: var(--text-muted); margin-bottom: 1rem;">
                    Use this to correct the total BTC holdings if they don't match your wallet
                </p>
                <div class="grid grid-2" style="gap: 1rem;">
                    <div>
                        <label>Current System Holdings</label>
                        <input type="text" id="currentHoldings" class="form-control" readonly>
                    </div>
                    <div>
                        <label>Correct Holdings (from wallet)</label>
                        <input type="text" id="correctHoldings" class="form-control" placeholder="0.00000000">
                    </div>
                </div>
                <button onclick="updateHoldings()" class="btn btn-primary" style="margin-top: 1rem;">
                    Update Holdings
                </button>
            </div>

            <!-- Recent Purchases -->
            <div class="card" style="margin-bottom: 2rem;">
                <h2 class="card-title">Recent BTC Purchases (Last 10)</h2>
                <div id="recentPurchases" style="max-height: 400px; overflow-y: auto;">
                    <!-- Will be populated -->
                </div>
            </div>

            <!-- Delete Last Purchase -->
            <div class="card" style="background: rgba(214, 39, 24, 0.1);">
                <h2 class="card-title" style="color: var(--accent-red);">Delete Last Purchase</h2>
                <p style="color: var(--text-muted);">
                    This will remove the most recent BTC purchase entry. Use with caution!
                </p>
                <div id="lastPurchaseInfo" style="margin: 1rem 0; padding: 1rem; background: white; border-radius: 8px;">
                    <!-- Will be populated -->
                </div>
                <button onclick="deleteLastPurchase()" class="btn btn-primary" style="background: var(--accent-red);">
                    Delete Last Purchase
                </button>
            </div>
        </div>
    </div>
</section>

<script>
const correctPIN = '2580';
let purchasesData = [];

// PIN verification
document.querySelectorAll('#pinModal input').forEach((input, index) => {
    input.addEventListener('input', (e) => {
        if (e.target.value && index < 3) {
            document.querySelector(`#pin${index + 2}`).focus();
        }
        if (index === 3 && e.target.value) {
            checkPIN();
        }
    });
});

function checkPIN() {
    const pin = document.getElementById('pin1').value + 
                document.getElementById('pin2').value + 
                document.getElementById('pin3').value + 
                document.getElementById('pin4').value;
    
    if (pin === correctPIN) {
        document.getElementById('pinModal').style.display = 'none';
        document.getElementById('mainContent').style.display = 'block';
        loadData();
    } else {
        // Clear and reset
        for (let i = 1; i <= 4; i++) {
            document.getElementById(`pin${i}`).value = '';
        }
        document.getElementById('pin1').focus();
    }
}

async function loadData() {
    try {
        // Load current holdings
        const summaryResponse = await fetch('/api/fund/summary');
        const summary = await summaryResponse.json();
        
        document.getElementById('currentHoldings').value = summary.total_btc_acquired.toFixed(8);
        document.getElementById('correctHoldings').placeholder = summary.total_btc_acquired.toFixed(8);
        
        // Load purchase history
        const historyResponse = await fetch('/api/fund/history');
        const history = await historyResponse.json();
        
        purchasesData = history.btc_purchases;
        
        // Show last 10 purchases
        const recentPurchases = purchasesData.slice(-10).reverse();
        const purchasesHtml = recentPurchases.map((purchase, index) => `
            <div class="member-card" style="margin-bottom: 0.5rem;">
                <div style="flex: 1;">
                    <div style="font-weight: 600;">
                        ${new Date(purchase.date).toLocaleDateString()} - ${purchase.btc_bought.toFixed(8)} BTC
                    </div>
                    <div style="color: var(--text-muted);">
                        Price: R${purchase.price_zar.toLocaleString()} | 
                        Total after: ${purchase.total_holdings.toFixed(8)} BTC
                    </div>
                    ${purchase.type === 'withdrawal' ? 
                        `<div style="color: var(--accent-red);">Withdrawal: ${purchase.member}</div>` : 
                        ''}
                </div>
            </div>
        `).join('');
        
        document.getElementById('recentPurchases').innerHTML = purchasesHtml;
        
        // Show last purchase info
        const lastPurchase = purchasesData[purchasesData.length - 1];
        if (lastPurchase) {
            document.getElementById('lastPurchaseInfo').innerHTML = `
                <strong>Date:</strong> ${new Date(lastPurchase.date).toLocaleDateString()}<br>
                <strong>Amount:</strong> ${lastPurchase.btc_bought.toFixed(8)} BTC<br>
                <strong>Price:</strong> R${lastPurchase.price_zar.toLocaleString()}<br>
                <strong>Total After:</strong> ${lastPurchase.total_holdings.toFixed(8)} BTC
            `;
        }
        
    } catch (error) {
        console.error('Error loading data:', error);
    }
}

async function updateHoldings() {
    const newHoldings = parseFloat(document.getElementById('correctHoldings').value);
    if (!newHoldings || newHoldings <= 0) {
        alert('Please enter a valid BTC amount');
        return;
    }
    
    if (!confirm(`Update total holdings to ${newHoldings.toFixed(8)} BTC?`)) {
        return;
    }
    
    try {
        const response = await fetch('/api/corrections/holdings', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify({ new_holdings: newHoldings })
        });
        
        if (response.ok) {
            alert('Holdings updated successfully!');
            loadData();
        } else {
            alert('Error updating holdings');
        }
    } catch (error) {
        alert('Error updating holdings');
    }
}

async function deleteLastPurchase() {
    if (!confirm('Delete the last purchase entry? This cannot be undone!')) {
        return;
    }
    
    try {
        const response = await fetch('/api/corrections/delete-last', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'}
        });
        
        if (response.ok) {
            alert('Last purchase deleted successfully!');
            loadData();
        } else {
            alert('Error deleting purchase');
        }
    } catch (error) {
        alert('Error deleting purchase');
    }
}

// Initialize
document.getElementById('pin1').focus();
</script>
{% endblock %}'''

# Save template
with open('app/templates/corrections.html', 'w', encoding='utf-8') as f:
    f.write(corrections_template)

print("✅ Created corrections interface v1.0")
print("Features:")
print("- Manual holdings adjustment")
print("- View recent purchases")
print("- Delete last purchase")
print("- PIN protected (2580)")