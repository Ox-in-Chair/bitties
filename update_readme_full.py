# Update README.md with all current features and roadmap

with open('README.md', 'r', encoding='utf-8') as f:
    content = f.read()

# Find the Current Status section and update it
status_section = '''## ✅ Current Status (August 2025)

- ✅ App running at [http://localhost:5000](http://localhost:5000)
- ✅ Dashboard operational with premium styling
- ✅ Bitcoin API endpoints configured
- ✅ Database structure supports members and transactions
- ⚠️ Live Bitcoin price data not yet fully connected to dashboard
- ⚠️ Member management UI still in development'''

new_status = '''## ✅ Current Status (August 2025)

### Completed Features
- ✅ **Live Dashboard** - Real-time BTC prices (ZAR/USD) with 30-second refresh
- ✅ **Historical Data Import** - Complete member & transaction history from Oct 2021
- ✅ **PIN-Protected Purchase Form** - Secure BTC recording with 4-digit PIN (2580)
- ✅ **Payment Verification** - Ensures all members paid before allowing BTC purchase
- ✅ **BTC Calculator** - Quick simulation tool for purchase estimates
- ✅ **Manual Holdings Input** - Salad can verify exact total BTC after each purchase
- ✅ **Masters Tournament Styling** - Premium CSS with defined colour palette
- ✅ **Automated Documentation** - Git commits auto-update HANDOVER.md and README.md
- ✅ **Member Contribution Tracking** - Shows each member's total contributions
- ✅ **Rich Nischk Exit Handling** - Properly tracks BTC withdrawal (0.01323 BTC)

### System Capabilities
- **Current Holdings**: 0.11107669 BTC (as of July 2025)
- **Active Members**: 7 (after Rich's exit)
- **Total Contributions**: R99,600
- **Portfolio Value**: Updates live based on current BTC price
- **Data Persistence**: JSON files with full audit trail'''

content = content.replace(status_section, new_status)

# Update the Roadmap section
if '🔭 Roadmap' in content:
    roadmap_start = content.find('🔭 Roadmap')
    roadmap_end = content.find('\n##', roadmap_start + 1)
    
    new_roadmap = '''🔭 Roadmap

### ✅ Completed (Aug 2025)
- [x] Live BTC price integration
- [x] Historical data import system
- [x] Secure purchase recording
- [x] Payment tracking foundation
- [x] Automated documentation

### 🚧 In Progress
- [ ] Member Management Interface
  - Add/remove members with auto-calculations
  - Exit settlement calculations
  - Join fee calculations for new members
- [ ] Payment Capture System
  - Individual payment recording
  - Bulk payment import
  - Monthly reconciliation

### 📋 Next Up (Priority Order)
1. **Member Management UI** (20 mins)
   - View/add/edit members
   - Calculate exit settlements
   - Calculate entry fees

2. **Payment Recording** (20 mins)
   - Mark monthly payments
   - Bulk update capabilities
   - Payment history view

3. **Historical Charts** (30 mins)
   - Portfolio growth over time
   - BTC price history
   - Member contribution charts

4. **System Config Tab** (25 mins)
   - Set monthly contribution amounts
   - Effective date controls
   - Global settings management

5. **Ledger View** (20 mins)
   - Combined transaction history
   - Month-end BTC prices
   - Filterable date ranges

6. **Mobile Optimization** (15 mins)
   - Responsive design check
   - Touch-friendly controls
   - Single-hand operation

7. **Export Reports** (25 mins)
   - PDF generation
   - CSV exports
   - Tax reporting

### 🎯 Long-term Goals (2026+)
- Augusta trip cost tracking
- Automated price alerts
- Multi-currency support
- Mobile app version
- WhatsApp integration'''

    if roadmap_end == -1:
        roadmap_end = len(content)
    
    content = content[:roadmap_start] + new_roadmap + content[roadmap_end:]

# Update Features section with version info
if '### 1. Live Bitcoin Tracking' in content:
    features_section = content[content.find('### 1. Live Bitcoin Tracking'):content.find('### 2. Member Management')]
    
    new_features = '''### 1. Live Bitcoin Tracking
- Pulls **real-time BTC prices** in **ZAR** and **USD** from public APIs
- **30-second auto-refresh** on dashboard
- **Quick calculator** for instant BTC estimates
- **Manual price override** for specific purchase rates
- **Version**: API integration v1.0, Calculator v1.4'''
    
    content = content.replace(features_section, new_features + '\n\n')

# Write updated README
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(content)

print("✅ README.md comprehensively updated")
print("📝 Added all completed features")
print("📝 Updated roadmap with priorities")
print("📝 Included version tracking")