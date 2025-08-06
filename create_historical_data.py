import json
import os
from datetime import datetime

# Create historical data structure for Bitties using ACCURATE statement data
# Properly tracking member transitions and Rich Nischk's BTC withdrawal

# Members data with accurate dates
MEMBERS_DATA = [
    {"id": 1, "name": "Salad", "joined_date": "2021-10-01", "leave_date": None, "status": "active", "role": "admin"},
    {"id": 2, "name": "Just", "joined_date": "2021-10-01", "leave_date": None, "status": "active", "role": "member"},
    {"id": 3, "name": "Jan", "joined_date": "2021-10-01", "leave_date": None, "status": "active", "role": "member"},
    {"id": 4, "name": "Rich Nischk", "joined_date": "2021-10-01", "leave_date": "2024-08-31", "status": "left", "role": "member"},
    {"id": 5, "name": "Ox", "joined_date": "2021-10-01", "leave_date": None, "status": "active", "role": "member"},
    {"id": 6, "name": "Frank", "joined_date": "2021-10-01", "leave_date": "2023-09-30", "status": "left", "role": "member"},
    {"id": 7, "name": "Flanners", "joined_date": "2021-10-01", "leave_date": None, "status": "active", "role": "member"},
    {"id": 8, "name": "Jerry", "joined_date": "2021-10-01", "leave_date": None, "status": "active", "role": "member"},
    {"id": 9, "name": "Mearp", "joined_date": "2023-10-01", "leave_date": None, "status": "active", "role": "member"}
]

# BTC purchase data from accurate historical records
BTC_PURCHASES = [
    {"date": "2021-11-15", "btc_bought": 0.00361734, "total_holdings": 0.00361734, "price_zar": 903375.54},
    {"date": "2021-12-04", "btc_bought": 0.00136405, "total_holdings": 0.00498138, "price_zar": 736189.52},
    {"date": "2022-01-05", "btc_bought": 0.00209107, "total_holdings": 0.00707245, "price_zar": 590581.70},
    {"date": "2022-02-03", "btc_bought": 0.00272717, "total_holdings": 0.00979962, "price_zar": 661996.82},
    {"date": "2022-03-02", "btc_bought": 0.00228075, "total_holdings": 0.01208037, "price_zar": 664404.50},
    {"date": "2022-04-04", "btc_bought": 0.00235400, "total_holdings": 0.01443437, "price_zar": 582678.85},
    {"date": "2022-05-05", "btc_bought": 0.00262582, "total_holdings": 0.01739528, "price_zar": 495513.80},
    {"date": "2022-06-03", "btc_bought": 0.00338308, "total_holdings": 0.02078092, "price_zar": 323702.83},
    {"date": "2022-07-05", "btc_bought": 0.00481237, "total_holdings": 0.02559329, "price_zar": 387041.23},
    {"date": "2022-08-05", "btc_bought": 0.00406258, "total_holdings": 0.02965587, "price_zar": 342948.86},
    {"date": "2022-09-09", "btc_bought": 0.00443611, "total_holdings": 0.03409867, "price_zar": 351079.66},
    {"date": "2022-10-10", "btc_bought": 0.00446955, "total_holdings": 0.03857495, "price_zar": 375061.86},
    {"date": "2022-11-02", "btc_bought": 0.00424943, "total_holdings": 0.04282438, "price_zar": 293653.27},
    {"date": "2022-12-07", "btc_bought": 0.00538740, "total_holdings": 0.04821907, "price_zar": 281127.15},
    {"date": "2023-01-11", "btc_bought": 0.00527394, "total_holdings": 0.05349302, "price_zar": 402709.49},
    {"date": "2023-03-10", "btc_bought": 0.00847980, "total_holdings": 0.06197678, "price_zar": 506241.02},
    {"date": "2023-06-06", "btc_bought": 0.00939691, "total_holdings": 0.07138009, "price_zar": 573356.47},
    {"date": "2023-08-17", "btc_bought": 0.00578617, "total_holdings": 0.07717337, "price_zar": 488403.62},
    {"date": "2023-09-12", "btc_bought": 0.00312554, "total_holdings": 0.08030328, "price_zar": 509931.52},
    {"date": "2023-12-13", "btc_bought": 0.00606528, "total_holdings": 0.08637093, "price_zar": 772646.41},
    {"date": "2024-01-19", "btc_bought": 0.00198700, "total_holdings": 0.08836329, "price_zar": 792604.82},
    {"date": "2024-02-15", "btc_bought": 0.00291496, "total_holdings": 0.09127825, "price_zar": 1181128.42},
    {"date": "2024-03-15", "btc_bought": 0.00237698, "total_holdings": 0.09365523, "price_zar": 1344669.95},
    {"date": "2024-04-15", "btc_bought": 0.00252379, "total_holdings": 0.09617902, "price_zar": 1140800.56},
    {"date": "2024-05-15", "btc_bought": 0.00250773, "total_holdings": 0.09868675, "price_zar": 1287787.83},
    {"date": "2024-06-15", "btc_bought": 0.00244615, "total_holdings": 0.10113290, "price_zar": 1097989.24},
    {"date": "2024-07-15", "btc_bought": 0.00262110, "total_holdings": 0.10375400, "price_zar": 1202938.47},
    {"date": "2024-08-15", "btc_bought": 0.00280010, "total_holdings": 0.10655410, "price_zar": 1055650.24},
    # Rich Nischk withdrawal event
    {"date": "2024-08-31", "btc_bought": 0.00000000, "total_holdings": 0.09332410, "price_zar": 1055650.24, "type": "withdrawal", "member": "Rich Nischk", "amount_withdrawn": 0.01323000},
    {"date": "2024-09-30", "btc_bought": 0.00240277, "total_holdings": 0.09572687, "price_zar": 1115359.62},
    {"date": "2024-10-15", "btc_bought": 0.00231302, "total_holdings": 0.09803989, "price_zar": 1272649.82},
    {"date": "2024-11-15", "btc_bought": 0.00166362, "total_holdings": 0.09970351, "price_zar": 1745313.47},
    {"date": "2024-12-15", "btc_bought": 0.00146100, "total_holdings": 0.10116451, "price_zar": 1745761.32},
    {"date": "2025-01-15", "btc_bought": 0.00145274, "total_holdings": 0.10261725, "price_zar": 1940377.77},
    {"date": "2025-02-15", "btc_bought": 0.00147154, "total_holdings": 0.10408879, "price_zar": 1501900.01},
    {"date": "2025-03-18", "btc_bought": 0.00175596, "total_holdings": 0.10584475, "price_zar": 1493218.01},
    {"date": "2025-05-14", "btc_bought": 0.00282588, "total_holdings": 0.10867063, "price_zar": 1865003.29},
    {"date": "2025-07-21", "btc_bought": 0.00264517, "total_holdings": 0.11107669, "price_zar": 1898877.75}
]

# Process contributions with accurate member periods
def process_contributions():
    contributions = []
    from datetime import datetime, timedelta
    
    # Generate monthly contributions based on member activity
    current_date = datetime(2021, 10, 1)
    end_date = datetime(2025, 7, 1)
    
    while current_date <= end_date:
        date_str = current_date.strftime("%Y-%m-%d")
        
        # Determine contribution amount for this month
        if current_date < datetime(2023, 12, 1):
            amount = 200
        elif current_date <= datetime(2024, 1, 1):
            amount = 300
        else:
            amount = 400
            
        # Process each member's contribution
        for member in MEMBERS_DATA:
            member_join = datetime.strptime(member['joined_date'], "%Y-%m-%d")
            
            # Skip if member hasn't joined yet
            if member_join > current_date:
                continue
                
            # Check if member has left
            if member['leave_date']:
                member_leave = datetime.strptime(member['leave_date'], "%Y-%m-%d")
                # Members contribute in their last month
                if current_date > member_leave:
                    continue
            
            contributions.append({
                "date": date_str,
                "member_id": member['id'],
                "member_name": member['name'],
                "amount_zar": amount,
                "type": "contribution"
            })
        
        # Move to next month
        if current_date.month == 12:
            current_date = current_date.replace(year=current_date.year + 1, month=1)
        else:
            current_date = current_date.replace(month=current_date.month + 1)
    
    return contributions

# Build the complete historical data structure
contributions = process_contributions()
historical_data = {
    "members": MEMBERS_DATA,
    "btc_purchases": BTC_PURCHASES,
    "contributions": contributions,
    "fund_info": {
        "name": "Augusta 2036 Bitcoin Fund",
        "target_date": "2036-04-01",
        "target_amount_zar": 1000000,
        "created_date": "2021-10-01",
        "description": "Pooled Bitcoin investment to fund Masters Tournament trip in 2036",
        "btc_purchaser": "Salad",
        "current_btc_holdings": 0.11107669,
        "last_purchase_date": "2025-07-21",
        "member_transitions": {
            "Frank_left": "2023-09-30",
            "Mearp_joined": "2023-10-01",
            "Rich_Nischk_left": "2024-08-31",
            "Rich_Nischk_btc_withdrawn": 0.01323000
        }
    }
}

# Calculate contribution summaries
member_contributions = {}
for member in MEMBERS_DATA:
    member_total = sum(c['amount_zar'] for c in contributions if c['member_id'] == member['id'])
    if member_total > 0:
        member_contributions[member['name']] = member_total

# Total contributions should be R99,600 as per statement
total_contributions = sum(member_contributions.values())

# Active members (7 currently active after Rich left)
active_members = [m for m in MEMBERS_DATA if m['status'] == 'active']

# Create data directory
os.makedirs('data', exist_ok=True)

# Save complete historical data
with open('data/historical_data.json', 'w') as f:
    json.dump(historical_data, f, indent=2)

# Create summary file
summary = {
    "total_contributions_zar": total_contributions,
    "total_btc_acquired": 0.11107669,
    "number_of_purchases": len([p for p in BTC_PURCHASES if p.get('type') != 'withdrawal']),
    "number_of_contributions": len(contributions),
    "active_members": len(active_members),
    "total_members_all_time": len(MEMBERS_DATA),
    "member_contributions": member_contributions,
    "current_share_per_member": round(0.11107669 / 7, 8),
    "data_updated": datetime.now().isoformat(),
    "last_btc_purchase": "2025-07-21",
    "portfolio_value_31_july": 234314.11,
    "rich_nischk_withdrawal": {
        "date": "2024-08-31",
        "btc_amount": 0.01323000,
        "reason": "Member exit - took proportional share"
    }
}

with open('data/fund_summary.json', 'w') as f:
    json.dump(summary, f, indent=2)

print("✅ Historical data created with ACCURATE member transitions!")
print(f"\n📊 Fund Summary (as of 31 July 2025):")
print(f"Total Contributions: R{total_contributions:,.2f}")
print(f"Total BTC Holdings: {0.11107669:.8f} BTC")
print(f"Portfolio Value: R234,314.11")
print(f"Profit: R{234314.11 - total_contributions:.2f} ({((234314.11 - total_contributions)/total_contributions * 100):.1f}%)")
print(f"\n👥 Member Status:")
print(f"Active Members: {len(active_members)} (Equal shares)")
print(f"BTC per Active Member: {0.11107669/7:.8f} BTC")
print(f"\n💰 Member Contributions:")
for name, amount in sorted(member_contributions.items(), key=lambda x: x[1], reverse=True):
    status = "Active" if name not in ["Frank", "Rich Nischk"] else "Left"
    if name == "Frank":
        status += " (Sep 2023, replaced by Mearp)"
    elif name == "Rich Nischk":
        status += f" (Aug 2024, withdrew {0.01323000:.8f} BTC)"
    print(f"{name}: R{amount:,.2f} ({status})")

print(f"\n📈 Key Events:")
print(f"• Fund started: October 2021 (8 members)")
print(f"• Frank left: September 2023")
print(f"• Mearp joined: October 2023 (maintained 8 members)")
print(f"• Rich Nischk left: August 2024 (withdrew BTC, down to 7 members)")
print(f"• Last BTC Purchase: 21 July 2025")
print(f"\n📁 Data saved to:")
print("- data/historical_data.json")
print("- data/fund_summary.json")