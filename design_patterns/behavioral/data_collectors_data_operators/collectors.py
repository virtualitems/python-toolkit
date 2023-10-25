"""
módulo de recolectores de datos

los recoclectores de datos son algoritmos que se encargan de extraer datos de
cualquier fuente, ya sea una base de datos, un archivo, una API, etc. y
convertirlos en una colección de datos (List, Dict, Tuple, etc.)
que pueda ser procesada por el programa.
"""

from __future__ import annotations
from typing import List

from entities import User


USERS = [
    User(name='john', email='jhon@email.com', subscription_days=30),
    User(name='jane', email='jane@email.com', subscription_days=30),
    User(name='mark', email='mark@email.com', subscription_days=0),
    User(name='sarah', email='sarah@email.com', subscription_days=0),
]


def list_all_users() -> List[User]:
    """Lista todos los usuarios"""
    return USERS


def list_users_without_subscription() -> List[User]:
    """Lista todos los usuarios sin suscripción"""
    return [user for user in USERS if user.subscription_days == 0]
