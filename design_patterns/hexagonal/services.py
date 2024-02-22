# -*- coding: utf-8 -*-

"""
Ports module
"""

# standard
from __future__ import annotations


class UserService:
    """User service"""

    def __init__(self, repository):
        self.repository = repository

    def list(self):
        """Get all users"""
        return self.repository.all()

    def create(self, user):
        """Create a user"""
        self.repository.create(user)

    def delete(self, user):
        """Delete a user"""
        self.repository.delete(user)
