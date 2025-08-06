README file for your "Bitties" App Build
# Bitties App

## Project Overview

**Bitties** is an innovative online mobile and web application designed to help a close-knit group of friends track their shared Bitcoin investments, which commenced in 2022. The app provides **live updates on contribution status**, **real-time Bitcoin charts**, and **dedicated member tabs** to foster transparency and engagement within the group.

Our vision is to build a robust and user-friendly application that simplifies the management and monitoring of our collective Bitcoin pool, while also offering advanced analytical and planning tools.

## Core Features

The Bitties app is engineered with a comprehensive set of features to meet the diverse needs of its users:

*   **Dual-Currency Dashboard**: Instantly toggle all charts and values between ZAR and USD for comprehensive financial oversight.
*   **Personal & Group Dashboards**: View individual contributions and performance alongside collective group totals, BTC holdings, portfolio value, and overall goal progress.
*   **Trader Analytics**: Access live and historic BTC charts (candlestick, line, area), contribution/balance graphs, Profit & Loss (P&L), volatility, drawdown, and various timeframes (1D, 1W, 1M, YTD, All). Track goal progress and performance against target trajectories.
*   **Speculation Tool**: Utilise a "what-if" simulator to explore scenarios based on contribution amounts, BTC price fluctuations, inflation, trip costs, and member count. Instantly update forecasts and export/share scenarios.
*   **Manual BTC Entry**: Authorised persons can add new Bitcoin purchases via a single, accessible form, which then automatically splits the value across the member pool.
*   **Notifications**: Receive timely email and (where possible) WhatsApp reminders for contributions, milestone achievements, and crucial BTC price alerts.
*   **Membership Management**: Easily manage member join/leave events, fairly adjust shares, support various user roles (admin/member/viewer), assign nicknames/avatars, and maintain a comprehensive audit log.
*   **Trip Goal Logic**: Automatically track and dynamically update savings goals for the Augusta 2036 trip, integrating live flight, accommodation, and ticket cost data via API-based refresh and scenario simulation.
*   **Mobile Responsive Design**: The entire dashboard and all UI elements are meticulously optimised for seamless use on both desktop and mobile/touch devices.

## Design Principles & User Experience

The Bitties app prioritises an intuitive, accessible, and aesthetically pleasing user experience, echoing the premium, elegant aesthetic of the Masters Tournament.

*   **Accessibility-First Controls**: All actions are designed for **single-tap/click operation** and are **accessibility friendly**, including one-click navigation for both mobile and desktop. The app allows for **full use by someone with only one hand and limited typing ability**.
*   **Zero Manual Setup**: **All data structure creation, migration, and completion are 100% automated**, ensuring the user is never prompted to manually set up or configure anything. The aim is a **"single upload, everything works"** deployment.
*   **Modular Architecture**: The application is built with a modular design to facilitate **future feature additions** and robust extensibility.
*   **Global Styling**: All user interface styling, including fonts, typography, and colours, is organised in a separate module. This allows for **global styling changes by modifying only the styling module**, without altering the core app code.
*   **Typography**: All text consistently uses the **"Poppins" font**.
*   **Colour Palette**: Inspired by the Masters Tournament, the app uses a clean and purposeful colour palette:
    *   **Primary Blue (`#0656A3`)**: Dominant brand and navigation colour, used for app bars, primary buttons, links, key highlights, headings, and actionable text.
    *   **Accent Green (`#00722D`)**: For success messages, progress indicators, and positive highlights.
    *   **Accent Yellow (`#FFB81C`)**: Used sparingly for alerts, warnings, or notification badges, accent lines, separators, or call-to-action highlights.
    *   **Accent Red (`#D62718`)**: Applied for errors, destructive actions, or urgent notifications, status indicators, or confirmation of critical actions.
    *   **Backgrounds**: Primary background is **White (`#FFFFFF`)** for clarity, with **Very Light Grey (`#F6F7FB`)** for cards, surfaces, or sections to reduce visual fatigue.
    *   **Text Colours**: Primary text uses the brand blue (`#0656A3`) for headings and key text, while body text considers **soft black (`#242424`)** or dark grey for optimal readability. All text ensures **WCAG AA/AAA contrast for accessibility**.
*   **Modern UI Touches (2025)**: Incorporates **rounded corners (12-20px radius)** for cards and buttons, **subtle drop-shadows** for elevation, **smooth micro-interactions** on hover/focus states, and **generous padding and margins** for a clean, uncluttered interface.
*   **Robustness**: The app is designed to be robust against missing, incomplete, or inconsistent data.

## Technology Considerations

The app will be built using either **Python or PowerShell** for its backend logic and functionality. **GitHub** will be utilised for version control and collaboration, and **Cloudflare** can be integrated for enhanced performance and security.

## Data Sources

The app relies on live and historical data from various public APIs and web scraping:

*   **Bitcoin Price Data**: Current and historical BTC price data (ZAR and USD) will be pulled from public APIs such as **CoinGecko and CryptoCompare**.
*   **Augusta 2036 Trip Costs**: Current and projected trip costs (flights, accommodation, tickets, spending) will be retrieved via **live web scraping and APIs** where possible.
*   All live data will **update regularly and automatically**.

## Development Guidelines & Maintenance

*   **Modular Build**: The project structure will be modular, with clear separation of concerns, particularly for styling and core logic.
*   **Version Control**: Any errors that arise will lead to a change in version.
*   **Documentation**: The `README.md` file will be continuously updated.
*   **Token Efficiency**: All development and communication will maintain token efficiency, especially considering token upload limits for GPT chats and build handover briefs.
*   **Automated Output**: Any script output will be provided as a **single block** ready for copy-pasting, eliminating the need for manual folder or file creation.
*   **No User Input During Execution**: All actions and logic within the app and its build scripts will be **automated and documented**, without prompting the user for input during code execution.
*   **Language & Formatting**: All app outputs will use **UK English spelling**, **UK number/date formats**, and **professional but friendly language**.
*   **Chart Presentation**: Each chart will be wrapped in a fluid container.

