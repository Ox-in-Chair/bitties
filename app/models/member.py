
# Save this as: app/models/member.py

"""Member Model"""
from dataclasses import dataclass
from datetime import datetime
from typing import Optional
import json

@dataclass
class Member:
    """Represents a member in the Bitcoin pool"""
    id: str
    name: str
    nickname: Optional[str] = None
    email: str = ""
    phone: Optional[str] = None
    role: str = "member"  # admin, member, viewer
    join_date: str = ""
    status: str = "active"  # active, inactive
    total_contributed: float = 0.0
    btc_balance: float = 0.0
    
    def __post_init__(self):
        if not self.join_date:
            self.join_date = datetime.now().isoformat()
    
    def to_dict(self):
        """Convert to dictionary"""
        return {
            'id': self.id,
            'name': self.name,
            'nickname': self.nickname,
            'email': self.email,
            'phone': self.phone,
            'role': self.role,
            'join_date': self.join_date,
            'status': self.status,
            'total_contributed': self.total_contributed,
            'btc_balance': self.btc_balance
        }
    
    @classmethod
    def from_dict(cls, data):
        """Create from dictionary"""
        return cls(**data)