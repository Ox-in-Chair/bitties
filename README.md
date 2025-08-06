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

#### Phase 1: Core Functionality (Next Sprint)

1. **Member Management UI** (20 mins)
   - Add/remove member interface
   - Automatic exit settlements
   - Join fee calculations

2. **Payment Capture System** (20 mins)
   - Mark monthly payments received
   - Bulk payment updates
   - Payment history tracking

3. **System Configuration** (25 mins)
   - Monthly contribution amounts
   - Effective date settings
   - Global preferences

#### Phase 2: Professional Trading Analytics

**Portfolio Performance Tab**
1. **Fund vs Market** - Compare Bitties performance vs BTC, S&P500, JSE
2. **Drawdown Analysis** - Maximum drawdown periods and recovery times
3. **Risk-Adjusted Returns** - Sharpe ratio, Sortino ratio over time
4. **Correlation Matrix** - BTC vs Gold, USD/ZAR, JSE, Commodities

**Member Analytics Tab**
5. **Contribution Flow** - Sankey diagram of money flow into BTC
6. **Member Performance** - Individual ROI based on entry timing
7. **Cost Basis Analysis** - Average purchase price per member

**Market Analysis Tab**
8. **Multi-Crypto Dashboard** - BTC, ETH, BNB, SOL, XRP in ZAR & USD
9. **Technical Indicators** - RSI, MACD, Bollinger Bands for BTC
10. **Volume Profile** - Price levels with highest trading volume

**ZAR Analysis Tab**
11. **USD/ZAR Impact** - How forex affects portfolio value
12. **Rand Hedging** - BTC as inflation hedge visualization
13. **Local Premium** - SA exchange premium vs international

#### Phase 3: Multi-Asset Comparison

**Crypto Comparison Tab**
- Live prices: BTC, ETH, BNB, SOL, XRP, ADA (ZAR & USD)
- 24h/7d/30d performance comparison
- Market cap rankings
- Dominance charts

**Traditional Markets Tab**
- JSE Top 40 vs Bitties fund
- Gold vs BTC correlation
- S&P 500 comparison
- Commodity index tracking

#### Phase 4: News & Information Feeds

**SA Sports News Tab**
- Springbok Rugby (RSS: sarugby.co.za)
- Proteas Cricket (RSS: cricket.co.za)
- Bafana Bafana Football
- SA Golf Tour updates

**Global Sports Tab**
- World Golf (PGA, Masters updates)
- International Rugby (Six Nations, World Cup)
- Cricket (IPL, Ashes)
- Tennis (Grand Slams)

**Financial News Tab**
- Crypto headlines (CoinDesk, Cointelegraph)
- Forex updates (focus on ZAR pairs)
- JSE & emerging markets
- Commodity prices

**SA Specific Tab**
- Load shedding schedule
- Cape Town weather (7-day forecast)
- Fuel price updates
- Interest rate announcements

#### Phase 5: SA-Relevant Interactive Features

**Trading Ideas Section**
- Crypto arbitrage opportunities (Luno vs international)
- Stablecoin yield farming tracker
- DeFi protocol comparison
- Tax optimization strategies (SA specific)

**Lifestyle Integration**
- "Beers to BTC" calculator (Castle price → Sats)
- Braai fund tracker (social events funded by gains)
- Golf day calculator (rounds affordable with profits)
- Rugby World Cup 2027 savings tracker

**Professional Tools**
- Tax report generator (SARS compatible)
- Forex impact calculator
- Inflation adjustment tool
- Estate planning projections

**Market Timing**
- Best day/time to buy analysis
- Payday investment optimizer
- Bonus allocation suggestions
- School fee planning with crypto

### 🎯 Design Principles

1. **Professional Focus** - Trading analysis, not games
2. **SA Context** - Rand, local exchanges, tax implications  
3. **Modular Tabs** - Clean separation by function
4. **Mobile Responsive** - Works on phone during load shedding
5. **Offline Capability** - Critical data cached locally### 🎮 Feature Design Principles

1. **Modular Tabs** - Each feature on separate tab
2. **Theme Grouping** - Related features clustered
3. **Masters Styling** - Consistent green/gold theme
4. **Mobile First** - Touch-optimized controls
5. **Real-time Updates** - Live data where applicable
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


### Update: 2025-08-07 01:41
- Restructured config features into tabbed interface (v1.0). Member Setup and Corrections now sub-tabs under Config. Fixed 404 error. Single PIN protection for all admin features.


### Update: 2025-08-07 01:24
- Fixed dashboard live updates (v1.1), added Corrections interface (v1.0) for data fixes, renamed Members to Member Setup. Dashboard now refreshes after purchases.


### Update: 2025-08-07 01:15
- Added Member Management UI (v1.0): View members, add with entry fee calculation, remove with BTC settlement. PIN protected. Tracks all member transitions.


### Update: 2025-08-07 01:08
- Redesigned roadmap for SA professional traders (v1.7): Serious analytics, multi-crypto tracking, separate news tabs, SA-specific features like load shedding and Luno arbitrage. No gamification.


### Update: 2025-08-07 01:03
- Added comprehensive interactive features to roadmap (v1.6): 10 visualization graphs, trading widgets, 8 RSS feeds, and engagement features. Organized in modular tab structure with Masters theme.


### Update: 2025-08-07 00:54
- Updated documentation to reflect ALL calculator issues are FIXED (v1.5). BTC calculator now fully functional with editable fields, proper formatting, and working calculations. No known issues remain.


### Update: 2025-08-07 00:54
- Comprehensive project status update: Documented all completed features (dashboard v1.0, transactions v1.4), known calculator issues, and prioritized outstanding features. Created PROJECT_STATUS.json for tracking.
