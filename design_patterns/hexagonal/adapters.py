# -*- coding: utf-8 -*-

"""
Ports module
"""

# standard
from __future__ import annotations
import sqlite3

# first-party
from ports import UserRepository


class Sqlite3UserRepository(UserRepository):
    """
    Adaptador que se implementa como un repositorio de usuarios

    """
    database_name = None
    connection = None
    table_name = 'users'

    def __init__(self, database_name):
        self.connection = sqlite3.connect(database_name)

    def get_cursor(self):
        return self.connection.cursor()

    def all(self):
        """Get all users"""
        cursor = self.get_cursor()
        cursor.execute(f'SELECT * FROM {self.table_name}')
        registros = cursor.fetchall()
        cursor.close()
        return registros

    def create(self, user):
        """Create a user"""
        cursor = self.get_cursor()
        cursor.execute(f'INSERT INTO {self.table_name} (name) VALUES (?)', (user.name,))
        self.connection.commit()
        cursor.close()

    def delete(self, user):
        """Delete a user"""
        cursor = self.get_cursor()
        cursor.execute(f'DELETE FROM {self.table_name} WHERE id = ?', (user.id,))
        self.connection.commit()
        cursor.close()
