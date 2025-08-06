\# Bitties - Bitcoin Investment Tracker

markdown# Bitties - Bitcoin Investment Tracker

Augusta 2036 Masters Tournament Fund Tracker

## Current Status
- ✅ Dashboard working at http://localhost:5000/dashboard
- ✅ Premium Masters-themed CSS styling applied
- ✅ API endpoints ready for data
- ⏳ Connecting live Bitcoin prices

## Quick Start

venv\Scripts\activate
bitties_commands run

## Routes
- `/` - Home page  
- `/dashboard` - Main investment dashboard
- `/api/btc/price` - Live Bitcoin prices

A web application for tracking a shared Bitcoin investment fund among friends, with the goal of funding a trip to the Masters Tournament in Augusta in 2036.



\## Current Status (August 2025)



\- ✅ App running at http://localhost:5000

\- ✅ Dashboard loads with premium Masters-themed styling

\- ✅ API endpoints ready for Bitcoin price data

\- ✅ Database structure for members and transactions

\- ⏳ Need to connect live data to dashboard

\- ⏳ Need to add member management functionality



\## Features



\- \*\*Live Bitcoin Tracking\*\*: Monitor BTC prices in ZAR and USD

\- \*\*Member Management\*\*: Track individual contributions and ownership percentages

\- \*\*Investment Dashboard\*\*: View portfolio performance and progress toward Augusta 2036 goal

\- \*\*Transaction History\*\*: Record and view all Bitcoin purchases

\- \*\*Beautiful UI\*\*: Premium Masters Tournament-inspired design with Poppins font



\## Tech Stack



\- \*\*Backend\*\*: Python Flask

\- \*\*Frontend\*\*: HTML, CSS (Masters-themed), JavaScript

\- \*\*Database\*\*: SQLite (via DataManager)

\- \*\*APIs\*\*: Bitcoin price data integration

\- \*\*Styling\*\*: Custom CSS with Masters Tournament colours



\## Installation



1\. Clone the repository:

```bash

git clone https://github.com/Ox-in-Chair/bitties.git

cd bitties

```



2\. Create virtual environment:

```cmd

python -m venv venv

venv\\Scripts\\activate

```



3\. Install dependencies:

```cmd

pip install -r requirements.txt

```



4\. Run the application:

```cmd

bitties\_commands run

```

Or alternatively:

```cmd

python run.py

```



5\. Open browser to http://localhost:5000



\## Project Structure



```

bitties/

├── app/

│   ├── static/

│   │   └── css/

│   │       └── styles.css      # Masters-themed styling

│   ├── templates/

│   │   ├── base.html          # Base template

│   │   ├── index.html         # Home page

│   │   └── dashboard.html     # Main dashboard

│   ├── api/

│   │   └── btc\_data.py        # Bitcoin API integration

│   ├── services/

│   │   └── data\_manager.py    # Database management

│   └── main.py                # Flask application

├── requirements.txt

├── run.py                     # Application entry point

└── README.md                  # This file

```



\## Available Routes



\- `/` - Home page

\- `/dashboard` - Main investment dashboard

\- `/api/members` - Member management API

\- `/api/transactions` - Transaction API

\- `/api/portfolio` - Portfolio summary API

\- `/api/btc/price` - Current Bitcoin price

\- `/api/btc/history` - Price history



\## Colour Palette (Masters Tournament Theme)



\- Primary Blue: #0656A3

\- Accent Green: #00722D

\- Accent Yellow: #FFB81C

\- Accent Red: #D62718

\- Background: #F6F7FB

\- Pure White: #FFFFFF



\## Next Steps



1\. Connect live Bitcoin price feeds to dashboard

2\. Implement member addition interface

3\. Add transaction recording functionality

4\. Create portfolio analytics and projections

5\. Add progress tracking toward Augusta 2036 goal



\## Contributing



This is a private project for a closed group of friends tracking their Bitcoin investment for the 2036 Masters trip.



\## License



Private project - not for public distribution

