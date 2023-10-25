"""
System entities
"""

from dataclasses import dataclass


@dataclass
class User():
    """User entity"""
    name: str
    email: str
    subscription_days: int
