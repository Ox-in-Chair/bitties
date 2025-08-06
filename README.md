# Bitties - Bitcoin Investment Tracker

Augusta 2036 Masters Tournament Fund Tracker

## 📊 Project Status (August 2025)

### ✅ Completed Features

#### 1. **Live Dashboard** (v1.0)
- Real-time BTC prices in ZAR and USD
- 30-second automatic refresh
- Member contribution visualization  
- Portfolio value calculations
- Augusta 2036 progress tracking

#### 2. **Transaction Recording** (v1.4)
- PIN-protected purchase form (2580)
- Payment verification system
- Manual holdings input for accuracy
- Confirmation dialogs
- Automatic data persistence
- **BTC Calculator** with:
  - Editable price fields
  - Bidirectional calculations
  - Proper decimal formatting
  - Real-time estimates

#### 3. **Historical Data Management** (v1.0)
- Complete import from Oct 2021
- Member transitions tracked (Frank→Mearp)
- Rich Nischk exit with BTC withdrawal
- Full audit trail in JSON

#### 4. **Infrastructure** (v1.0)
- Automated commit with doc updates
- Masters Tournament theme (Poppins font)
- Git version tracking
- RESTful API endpoints

### ✅ All Known Issues Resolved

All previously identified calculator issues have been fixed in v1.4:
- BTC Price field now fully editable
- Decimal display working correctly (no 9e-8)
- Full keyboard input support
- All auto-calculations functioning

### 🚧 Outstanding Features (Priority Order)

1. **Member Management UI** (20 mins)
   - Add/remove member interface
   - Automatic exit settlements
   - Join fee calculations

2. **Payment Capture System** (20 mins)
   - Mark monthly payments received
   - Bulk payment updates
   - Payment history tracking

3. **Historical Charts** (30 mins)
   - Portfolio growth visualization
   - BTC price trends
   - Member contribution graphs

4. **System Configuration** (25 mins)
   - Monthly contribution amounts
   - Effective date settings
   - Global preferences

5. **Ledger View** (20 mins)
   - Full transaction history
   - Month-end BTC prices
   - Date range filtering

6. **Mobile Optimization** (15 mins)
   - Responsive design fixes
   - Touch-friendly controls
   - Single-hand operation

7. **Export Reports** (25 mins)
   - PDF statements
   - CSV data export
   - Tax documentation

## 🎯 Technical Specifications

- **Current BTC Holdings**: 0.11107669 BTC
- **Active Members**: 7
- **Total Contributions**: R99,600
- **Last Purchase**: 21 July 2025
- **PIN Code**: 2580
- **Tech Stack**: Flask, JavaScript, JSON storage

## 🚀 Quick Start

```bash
cd C:\Users\mike\OneDrive\BitcoinApp\bitties
venv\Scripts\activate
bitties_commands run
```

Access at: http://localhost:5000/dashboard

## 📁 Key Files

- `app/main.py` - Flask application (v1.3)
- `app/templates/dashboard.html` - Main interface
- `app/templates/transaction_form.html` - Purchase recording (v1.4)
- `data/historical_data.json` - Complete transaction history
- `data/fund_summary.json` - Current fund state
## Development Progress


### Update: 2025-08-07 00:54
- Updated documentation to reflect ALL calculator issues are FIXED (v1.5). BTC calculator now fully functional with editable fields, proper formatting, and working calculations. No known issues remain.


### Update: 2025-08-07 00:54
- Comprehensive project status update: Documented all completed features (dashboard v1.0, transactions v1.4), known calculator issues, and prioritized outstanding features. Created PROJECT_STATUS.json for tracking.
