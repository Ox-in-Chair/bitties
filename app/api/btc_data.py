# Save this as: app/api/btc_data.py

"""Bitcoin Data API Integration"""
import requests
from datetime import datetime
from typing import Dict, List

def get_current_btc_price() -> Dict:
    """Get current BTC price in ZAR and USD"""
    try:
        # Try CoinGecko API (free tier)
        response = requests.get(
            "https://api.coingecko.com/api/v3/simple/price",
            params={
                'ids': 'bitcoin',
                'vs_currencies': 'zar,usd',
                'include_24hr_change': 'true'
            },
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()['bitcoin']
            return {
                'zar': data['zar'],
                'usd': data['usd'],
                'zar_24h_change': data.get('zar_24h_change', 0),
                'usd_24h_change': data.get('usd_24h_change', 0),
                'timestamp': datetime.now().isoformat(),
                'source': 'coingecko'
            }
    except Exception as e:
        print(f"Error fetching BTC price: {e}")
    
    # Return mock data as fallback
    return {
        'zar': 532000,
        'usd': 35000,
        'zar_24h_change': 2.5,
        'usd_24h_change': 2.5,
        'timestamp': datetime.now().isoformat(),
        'source': 'mock'
    }

def get_btc_history(days: int = 30) -> List[Dict]:
    """Get historical BTC price data"""
    try:
        response = requests.get(
            f"https://api.coingecko.com/api/v3/coins/bitcoin/market_chart",
            params={
                'vs_currency': 'zar',
                'days': days
            },
            timeout=10
        )
        
        if response.status_code == 200:
            data = response.json()
            prices = []
            for timestamp, price in data['prices']:
                prices.append({
                    'timestamp': datetime.fromtimestamp(timestamp/1000).isoformat(),
                    'price_zar': price,
                    'price_usd': price / 15.2  # Approximate conversion
                })
            return prices
    except Exception as e:
        print(f"Error fetching history: {e}")
    
    # Return mock data
    return []