import shutil

# Create the transaction recording template
transaction_template = '''{% extends "base.html" %}
{% block title %}Bitties - Record BTC Purchase{% endblock %}
{% block content %}
<section class="section">
    <div class="container">
        <h1 style="color: var(--primary-blue); margin-bottom: 2rem;">Record Bitcoin Purchase</h1>
        
        <!-- PIN Protection Modal -->
        <div id="pinModal" class="modal active">
            <div class="modal-content" style="max-width: 400px;">
                <h2 style="text-align: center; margin-bottom: 1.5rem;">Enter PIN to Continue</h2>
                <div style="display: flex; justify-content: center; gap: 10px; margin-bottom: 1.5rem;">
                    <input type="password" id="pin1" maxlength="1" style="width: 50px; height: 50px; text-align: center; font-size: 24px;" class="form-control">
                    <input type="password" id="pin2" maxlength="1" style="width: 50px; height: 50px; text-align: center; font-size: 24px;" class="form-control">
                    <input type="password" id="pin3" maxlength="1" style="width: 50px; height: 50px; text-align: center; font-size: 24px;" class="form-control">
                    <input type="password" id="pin4" maxlength="1" style="width: 50px; height: 50px; text-align: center; font-size: 24px;" class="form-control">
                </div>
                <div id="pinError" style="color: var(--accent-red); text-align: center; margin-bottom: 1rem; display: none;">
                    Incorrect PIN. Try again.
                </div>
                <button onclick="checkPIN()" class="btn btn-primary" style="width: 100%;">Submit</button>
            </div>
        </div>

        <!-- Main Form (hidden until PIN verified) -->
        <div id="mainContent" style="display: none;">
            <!-- Current Status -->
            <div class="card" style="margin-bottom: 2rem;">
                <h2 class="card-title">Current Fund Status</h2>
                <div class="grid grid-4">
                    <div class="stat-card">
                        <div class="stat-label">Current BTC Holdings</div>
                        <div class="stat-value" id="current-btc">Loading...</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-label">Available to Invest</div>
                        <div class="stat-value" id="available-funds">Loading...</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-label">Current BTC Price</div>
                        <div class="stat-value" id="btc-price">Loading...</div>
                    </div>
                    <div class="stat-card">
                        <div class="stat-label">Est. BTC to Buy</div>
                        <div class="stat-value" id="est-btc">0.00000000</div>
                    </div>
                </div>
            </div>

            <!-- Payment Status Check -->
            <div class="card" style="margin-bottom: 2rem;">
                <h2 class="card-title">Member Payment Status</h2>
                <div id="payment-status" class="grid grid-3">
                    <!-- Will be populated by JavaScript -->
                </div>
                <div id="payment-warning" class="alert" style="background: var(--accent-yellow); padding: 1rem; border-radius: 8px; margin-top: 1rem; display: none;">
                    ⚠️ Not all members have paid. Complete all payments before purchasing BTC.
                </div>
            </div>

            <!-- Purchase Form -->
            <div class="card">
                <h2 class="card-title">Record New Purchase</h2>
                <form id="purchaseForm" onsubmit="recordPurchase(event)">
                    <div class="grid grid-2" style="gap: 1rem; margin-bottom: 1rem;">
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem;">Purchase Date</label>
                            <input type="date" id="purchaseDate" class="form-control" required>
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem;">BTC Price (ZAR)</label>
                            <input type="number" id="btcPriceInput" class="form-control" step="0.01" required>
                        </div>
                    </div>
                    
                    <div class="grid grid-2" style="gap: 1rem; margin-bottom: 1rem;">
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem;">Amount to Invest (ZAR)</label>
                            <input type="number" id="amountZAR" class="form-control" step="0.01" required>
                        </div>
                        <div>
                            <label style="display: block; margin-bottom: 0.5rem;">BTC to Purchase</label>
                            <input type="number" id="btcAmount" class="form-control" step="0.00000001" required readonly>
                        </div>
                    </div>
                    
                    <div style="margin-bottom: 1rem;">
                        <label style="display: block; margin-bottom: 0.5rem;">Notes (optional)</label>
                        <textarea id="notes" class="form-control" rows="2"></textarea>
                    </div>
                    
                    <button type="submit" class="btn btn-primary" id="submitBtn" disabled>
                        Record Purchase
                    </button>
                </form>
            </div>
        </div>
    </div>
</section>

<script>
// PIN verification (default: 2580)
const correctPIN = '2580';
let currentBTCPrice = 0;
let availableFunds = 0;
let allMembersPaid = false;

// Auto-advance PIN inputs
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
        loadFundStatus();
        loadPaymentStatus();
    } else {
        document.getElementById('pinError').style.display = 'block';
        // Clear inputs
        for (let i = 1; i <= 4; i++) {
            document.getElementById(`pin${i}`).value = '';
        }
        document.getElementById('pin1').focus();
    }
}

async function loadFundStatus() {
    try {
        // Load fund summary
        const fundResponse = await fetch('/api/fund/summary');
        const fundData = await fundResponse.json();
        
        document.getElementById('current-btc').textContent = fundData.total_btc_acquired.toFixed(8);
        
        // Load current BTC price
        const priceResponse = await fetch('/api/btc/price');
        const priceData = await priceResponse.json();
        
        currentBTCPrice = priceData.zar;
        document.getElementById('btc-price').textContent = `R${currentBTCPrice.toLocaleString()}`;
        document.getElementById('btcPriceInput').value = currentBTCPrice.toFixed(2);
        
        // Set today's date
        document.getElementById('purchaseDate').valueAsDate = new Date();
        
    } catch (error) {
        console.error('Error loading fund status:', error);
    }
}

async function loadPaymentStatus() {
    try {
        // Load payment status for current month
        const response = await fetch('/api/payments/current-month');
        const payments = await response.json();
        
        const container = document.getElementById('payment-status');
        let unpaidCount = 0;
        availableFunds = 0;
        
        const paymentHTML = payments.members.map(member => {
            const isPaid = member.paid;
            if (!isPaid) unpaidCount++;
            if (isPaid) availableFunds += member.amount;
            
            return `
                <div class="member-card" style="border: 2px solid ${isPaid ? 'var(--accent-green)' : 'var(--accent-red)'};">
                    <div class="member-avatar" style="background: ${isPaid ? 'var(--accent-green)' : 'var(--accent-red)'};">
                        ${member.initials}
                    </div>
                    <div>
                        <div style="font-weight: 600;">${member.name}</div>
                        <div style="color: ${isPaid ? 'var(--accent-green)' : 'var(--accent-red)'};">
                            ${isPaid ? '✓ Paid R' + member.amount : '✗ Not Paid'}
                        </div>
                    </div>
                </div>
            `;
        }).join('');
        
        container.innerHTML = paymentHTML;
        document.getElementById('available-funds').textContent = `R${availableFunds.toLocaleString()}`;
        
        // Show warning if not all paid
        if (unpaidCount > 0) {
            document.getElementById('payment-warning').style.display = 'block';
            document.getElementById('submitBtn').disabled = true;
            allMembersPaid = false;
        } else {
            document.getElementById('payment-warning').style.display = 'none';
            document.getElementById('submitBtn').disabled = false;
            allMembersPaid = true;
        }
        
        // Auto-fill amount if all paid
        if (allMembersPaid && availableFunds > 0) {
            document.getElementById('amountZAR').value = availableFunds.toFixed(2);
            calculateBTC();
        }
        
    } catch (error) {
        console.error('Error loading payment status:', error);
        // For now, allow purchase if API not ready
        document.getElementById('submitBtn').disabled = false;
        allMembersPaid = true;
    }
}

// Calculate BTC amount
document.getElementById('amountZAR').addEventListener('input', calculateBTC);
document.getElementById('btcPriceInput').addEventListener('input', calculateBTC);

function calculateBTC() {
    const amountZAR = parseFloat(document.getElementById('amountZAR').value) || 0;
    const btcPrice = parseFloat(document.getElementById('btcPriceInput').value) || currentBTCPrice;
    
    if (amountZAR > 0 && btcPrice > 0) {
        const btcAmount = amountZAR / btcPrice;
        document.getElementById('btcAmount').value = btcAmount.toFixed(8);
        document.getElementById('est-btc').textContent = btcAmount.toFixed(8);
    }
}

async function recordPurchase(event) {
    event.preventDefault();
    
    if (!allMembersPaid) {
        alert('All members must pay before recording a purchase.');
        return;
    }
    
    const purchaseData = {
        date: document.getElementById('purchaseDate').value,
        btc_price_zar: parseFloat(document.getElementById('btcPriceInput').value),
        amount_zar: parseFloat(document.getElementById('amountZAR').value),
        btc_amount: parseFloat(document.getElementById('btcAmount').value),
        notes: document.getElementById('notes').value
    };
    
    try {
        const response = await fetch('/api/btc/purchase', {
            method: 'POST',
            headers: {'Content-Type': 'application/json'},
            body: JSON.stringify(purchaseData)
        });
        
        if (response.ok) {
            alert('Purchase recorded successfully!');
            window.location.href = '/dashboard';
        } else {
            alert('Error recording purchase. Please try again.');
        }
    } catch (error) {
        console.error('Error:', error);
        alert('Error recording purchase. Please try again.');
    }
}

// Initialize
document.getElementById('pin1').focus();
</script>
{% endblock %}'''

# Save the template
with open('app/templates/transaction_form.html', 'w', encoding='utf-8') as f:
    f.write(transaction_template)

print("✅ Transaction form template created!")
print("Next: Adding routes to handle the form...")