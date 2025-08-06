# Augusta 2036 Masters Tournament Fund Tracker

## 📁 Project Path
This application resides at:  
`C:\Users\mike\OneDrive\BitcoinApp\bitties`  
GitHub repository: [https://github.com/Ox-in-Chair/bitties](https://github.com/Ox-in-Chair/bitties)

---

## 🧭 Overview
**Bitties** is a private mobile and web application designed to help a group of friends manage their shared Bitcoin investment fund, initiated in 2022. The fund’s ultimate goal is to fully finance a trip to the **Masters Tournament in Augusta, Georgia, in 2036**. The application provides a comprehensive suite of dashboards, live data integration, member-specific views, and historical transaction tracking, all wrapped in a premium, Masters-inspired UI.

---

## ✅ Current Status (August 2025)

- ✅ App running locally at [http://localhost:5000](http://localhost:5000)
- ✅ Dashboard operational with premium styling
- ✅ Bitcoin API endpoints configured
- ✅ Database structure supports members and transactions
- ⚠️ Live Bitcoin price data not yet fully connected to dashboard
- ⚠️ Member management UI still in development

---

## 🚀 Features

### 1. Live Bitcoin Tracking
- Pulls **real-time BTC prices** in **ZAR** and **USD** from public APIs (CoinGecko, CryptoCompare).
- Supports **candlestick, line, area charts** over timeframes: 1D, 1W, 1M, YTD, All.
- Dashboard toggle to switch between currencies instantly.
- Dual-currency charts with live updates.

### 2. Member Management
- View and manage members who’ve contributed since 2022.
- Assign roles (admin/member/viewer), nicknames, avatars.
- Audit trail for join/leave/transfer activity.
- Nicknames and profile avatars.
- Manual BTC entries (e.g., pooled purchase logs).
- Historical data stored externally (CSV/JSON/SQL) and referenced automatically.
- Accurate share allocations, dynamically adjusted.
- All data ingestion and migration is 100% automated and fault-tolerant.

### 3. Investment Dashboard
- Personal and group dashboards showing:
  - Total BTC held
  - Portfolio value
  - Goal progress
  - Contribution vs. balance graphs
  - Volatility, drawdown, P&L
- Real-time and historical performance comparison vs. Augusta 2036 savings goal.
- Cost tracking for flights, accommodation, and tickets via API/scraping.
- Simulation of scenarios (e.g. BTC price or member count changes).

### 4. Transaction History
- Secure, manual BTC entry via admin form.
- Records include purchase amount, timestamp, price, and memo.
- Automatic splitting of BTC among current members.
- Support for historical reconciliation (2021–2025 dataset).
- Full ledger continuity, with versioned snapshots.

### 5. Multiple UI Tabs
App is modular and grouped into themed tabs, accessible via mobile and desktop:
- 🏠 Home
- 📈 Dashboard
- 👤 Members
- 💸 Transactions
- 🎯 Goal Tracker
- ⚙️ Settings
- ❓ Help (with tooltips and guides)

### 6. Premium User Interface
Aesthetic and UX inspired by the **Masters Tournament**:
- **Font**: Poppins (CSS: `--font-family: 'Poppins', sans-serif`)
- **Rounded corners**: 12–20px on all cards and buttons
- **Drop shadows**: Subtle elevation styling
- **Animations**: Smooth hover/focus transitions
- **Responsive**: Optimised for both desktop and mobile
- **Accessibility-first**: Single-tap/click interaction, compliant with WCAG AA/AAA
- **Tooltips**: Clickable or hover-enabled "?" icons explaining each button or tab

#### 🎨 Colour Palette

| Purpose           | Colour Name     | Hex Code   | CSS Variable           |
|-------------------|------------------|------------|-------------------------|
| Primary           | Blue             | `#0656A3`  | `--primary-blue`        |
| Accent            | Green            | `#00722D`  | `--accent-green`        |
| Alert             | Yellow           | `#FFB81C`  | `--accent-yellow`       |
| Error             | Red              | `#D62718`  | `--accent-red`          |
| Background        | Light Grey       | `#F6F7FB`  | `--surface`             |
| Base Background   | White            | `#FFFFFF`  | `--background`          |
| Headings/Text     | Deep Blue/Black  | `#242424`  | `--text-main`           |

---

## 🛠️ Tech Stack

| Layer          | Stack / Tools                                 |
|----------------|------------------------------------------------|
| Backend        | Python (Flask), CMD                           |
| Frontend       | HTML, CSS (modular), JavaScript               |
| Styling        | `styles.css` (centralised, modular theme)     |
| Database       | SQLite (via `data_manager.py`)                |
| API Integrations| CoinGecko, CryptoCompare, scraping logic     |
| Deployment     | Single-block scripts (no manual setup)        |
| CDN            | Optional: Cloudflare                          |
| Versioning     | GitHub (https://github.com/Ox-in-Chair/bitties) |

---

## 📦 Installation

```bash
git clone https://github.com/Ox-in-Chair/bitties.git
cd bitties
cmd
Copy
Edit
python -m venv venv
venv\Scripts\activate
pip install -r requirements.txt
To run the app:

cmd
Copy
Edit
bitties_commands run
or:

cmd
Copy
Edit
python run.py
Open browser to:
http://localhost:5000

🔌 Available Routes
Route	Description
/	Home page
/dashboard	Investment dashboard
/api/members	Member management API
/api/transactions	BTC transaction log
/api/portfolio	Portfolio summary
/api/btc/price	Live BTC pricing (ZAR/USD)
/api/btc/history	Historical BTC price feed

📂 Project Structure
csharp
Copy
Edit
bitties/
├── app/
│   ├── static/
│   │   └── css/
│   │       └── styles.css           # Central UI styling
│   ├── templates/
│   │   ├── base.html                # Shared layout
│   │   ├── index.html               # Home
│   │   └── dashboard.html           # Dashboard
│   ├── api/
│   │   └── btc_data.py              # API for BTC pricing
│   ├── services/
│   │   └── data_manager.py          # DB handler
│   └── main.py                      # Flask entry
├── requirements.txt
├── run.py
└── README.md
🔭 Roadmap
MVP (Delivered / In Progress)
 Live dashboard UI

 Master-themed design

 Bitcoin API integration

 Modular CSS

 CLI-run and deploy scripts

Near-Term Goals (Q3–Q4 2025)
 Connect all endpoints to UI

 Finalise transaction entry forms

 Enable dynamic BTC sharing logic

 Tooltips on all user actions

 Uploadable logo branding

 Member transfer tracking and audit log

Mid-Term (2026)
 Goal trajectory analytics (AI-based)

 Budget simulation and BTC forecasting

 Full mobile app version

 Multi-language support (EN/AF)

 WhatsApp notification integration

🤝 Contributing
This is a private project managed by a closed group. Contributions are not accepted unless by invitation.

🔒 License
Private project. All code, content, and data are not for public use, distribution, or duplication. 
