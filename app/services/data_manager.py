# Save this as: app/services/data_manager.py

"""Data Management Service"""
import json
from pathlib import Path
from datetime import datetime
from typing import List, Optional, Dict
import uuid

class DataManager:
    """Manages all application data"""
    
    def __init__(self):
        self.data_dir = Path(__file__).parent.parent / 'data'
        self.data_dir.mkdir(exist_ok=True)
        
        self.members_file = self.data_dir / 'members.json'
        self.transactions_file = self.data_dir / 'transactions.json'
        
        self._init_data_files()
        self._load_data()
    
    def _init_data_files(self):
        """Initialize data files if they don't exist"""
        if not self.members_file.exists():
            self.members_file.write_text(json.dumps([], indent=2))
        
        if not self.transactions_file.exists():
            self.transactions_file.write_text(json.dumps([], indent=2))
    
    def _load_data(self):
        """Load data from files"""
        self.members = json.loads(self.members_file.read_text())
        self.transactions = json.loads(self.transactions_file.read_text())
    
    def _save_members(self):
        """Save members to file"""
        self.members_file.write_text(json.dumps(self.members, indent=2))
    
    def _save_transactions(self):
        """Save transactions to file"""
        self.transactions_file.write_text(json.dumps(self.transactions, indent=2))
    
    # Member operations
    def get_members(self) -> List[Dict]:
        """Get all members"""
        return self.members
    
    def get_member(self, member_id: str) -> Optional[Dict]:
        """Get member by ID"""
        for member in self.members:
            if member['id'] == member_id:
                return member
        return None
    
    def add_member(self, member_data: Dict) -> Dict:
        """Add new member"""
        member_data['id'] = str(uuid.uuid4())
        member_data['join_date'] = datetime.now().isoformat()
        member_data['total_contributed'] = 0
        member_data['btc_balance'] = 0
        
        self.members.append(member_data)
        self._save_members()
        return member_data
    
    # Transaction operations
    def get_transactions(self) -> List[Dict]:
        """Get all transactions"""
        return self.transactions
    
    def add_transaction(self, transaction_data: Dict) -> Dict:
        """Add new transaction"""
        # Auto-calculate BTC amount if not provided
        if 'amount_btc' not in transaction_data:
            btc_price = transaction_data.get('btc_price_zar', 532000)
            amount_zar = transaction_data.get('amount_zar', 0)
            transaction_data['amount_btc'] = amount_zar / btc_price
        
        # Add ID and date
        transaction_data['id'] = str(uuid.uuid4())
        transaction_data['date'] = datetime.now().isoformat()
        
        # Add USD price if not provided
        if 'btc_price_usd' not in transaction_data:
            transaction_data['btc_price_usd'] = transaction_data.get('btc_price_zar', 532000) / 15.2
        
        self.transactions.append(transaction_data)
        self._save_transactions()
        
        # Update member balances
        self._update_member_balances()
        
        return transaction_data
    
    def _update_member_balances(self):
        """Update member balances based on transactions"""
        # Reset balances
        for member in self.members:
            member['total_contributed'] = 0
            member['btc_balance'] = 0
        
        # Calculate from transactions
        for transaction in self.transactions:
            member = self.get_member(transaction['member_id'])
            if member and transaction['type'] in ['contribution', 'purchase']:
                member['total_contributed'] += transaction['amount_zar']
                member['btc_balance'] += transaction['amount_btc']
        
        self._save_members()
    
    def get_portfolio_summary(self) -> Dict:
        """Get portfolio summary"""
        total_btc = sum(m['btc_balance'] for m in self.members)
        total_invested = sum(m['total_contributed'] for m in self.members)
        
        return {
            'total_btc': total_btc,
            'total_invested_zar': total_invested,
            'member_count': len([m for m in self.members if m.get('status') == 'active']),
            'transaction_count': len(self.transactions)
        }