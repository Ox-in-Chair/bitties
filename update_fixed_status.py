# Update all documentation to reflect fixed calculator issues

import json
from datetime import datetime

# Update PROJECT_STATUS.json
with open('PROJECT_STATUS.json', 'r', encoding='utf-8') as f:
    status = json.load(f)

# Move calculator from known_issues to completed_features
status['completed_features']['btc_calculator'] = {
    "status": "✅ Complete",
    "version": "1.4",
    "features": [
        "BTC Price field fully editable",
        "Proper decimal display (no scientific notation)",
        "Direct keyboard input (not just arrows)",
        "Est. BTC to Buy auto-calculates",
        "BTC You'd Get computes from all inputs",
        "Bidirectional calculations (ZAR↔BTC)"
    ]
}

# Remove from known_issues
if 'btc_calculator' in status['known_issues']:
    del status['known_issues']['btc_calculator']

# If no more known issues, update the section
if not status['known_issues']:
    status['known_issues'] = {
        "none": {
            "status": "✅ All Clear",
            "issues": ["No known issues at this time"]
        }
    }

status['last_updated'] = datetime.now().isoformat()
status['current_version'] = "1.5"

# Save updated status
with open('PROJECT_STATUS.json', 'w', encoding='utf-8') as f:
    json.dump(status, f, indent=2)

# Update README
with open('README.md', 'r', encoding='utf-8') as f:
    readme = f.read()

# Replace the Known Issues section
old_issues = '''### ⚠️ Known Issues

1. **BTC Calculator Fields**
   - BTC Price field incorrectly read-only
   - Scientific notation (9e-8) display bug
   - Arrow-only input restriction
   - Auto-calculations not triggering'''

new_issues = '''### ✅ All Known Issues Resolved

All previously identified calculator issues have been fixed in v1.4:
- BTC Price field now fully editable
- Decimal display working correctly (no 9e-8)
- Full keyboard input support
- All auto-calculations functioning'''

readme = readme.replace(old_issues, new_issues)

# Update the completed features section
old_transaction = '''#### 2. **Transaction Recording** (v1.4)
- PIN-protected purchase form (2580)
- Payment verification system
- Manual holdings input for accuracy
- Confirmation dialogs
- Automatic data persistence'''

new_transaction = '''#### 2. **Transaction Recording** (v1.4)
- PIN-protected purchase form (2580)
- Payment verification system
- Manual holdings input for accuracy
- Confirmation dialogs
- Automatic data persistence
- **BTC Calculator** with:
  - Editable price fields
  - Bidirectional calculations
  - Proper decimal formatting
  - Real-time estimates'''

readme = readme.replace(old_transaction, new_transaction)

# Update version
readme = readme.replace('current_version": "1.4"', 'current_version": "1.5"')

# Save updated README
with open('README.md', 'w', encoding='utf-8') as f:
    f.write(readme)

# Update HANDOVER.md
handover_content = f'''# Bitties Project Handover
Last Updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}

## Current System Status - v1.5

### ✅ WORKING FEATURES
1. **Dashboard** - Live BTC prices, member contributions, portfolio tracking
2. **Transaction Recording** - PIN-protected, payment verification, manual holdings
3. **BTC Calculator** - ALL ISSUES FIXED:
   - Editable price fields ✅
   - No scientific notation ✅
   - Keyboard input works ✅
   - Auto-calculations work ✅
   - Bidirectional conversion ✅

### 🚧 NOT YET BUILT
1. Member Management UI
2. Payment Capture System
3. Historical Charts
4. System Configuration
5. Ledger View
6. Mobile Optimization
7. Export Reports

### 📊 Current Data
- BTC Holdings: 0.11107669
- Active Members: 7
- Total Invested: R99,600
- Last Purchase: 2025-07-21

### 🔧 Technical Notes
- PIN Code: 2580
- Version: 1.5 (Calculator fixes complete)
- All calculator fields now work properly
- No known bugs in existing features

### 📁 Key Files
- `transaction_form.html` (v1.4) - Has working calculator
- `main.py` (v1.3) - Handles purchase recording
- `dashboard.html` (v1.0) - Shows live data
'''

with open('HANDOVER.md', 'w', encoding='utf-8') as f:
    f.write(handover_content)

print("✅ Documentation updated to reflect FIXED status")
print("📝 PROJECT_STATUS.json - Calculator moved to completed")
print("📝 README.md - Known issues section updated")
print("📝 HANDOVER.md - Shows all features working")
print("📝 Version bumped to 1.5")