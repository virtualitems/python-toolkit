"""
módulo de operadores de datos

los operadores de datos son algoritmos que se encargan de procesar
los datos obtenidos por los recolectores para obtener un resultado.
Los operadores pueden o no generar una nueva colección de datos
a partir de la original.
"""

from __future__ import annotations
from typing import List

from entities import User


def send_email(user: User, message: str) -> None:
    """Envía un email a un usuario"""

    print(f'Sending email to {user.email} with message: {message}')


def send_gift(users: List[User]) -> None:
    """Envía un regalo a los usuarios"""

    for user in users:
        user.subscription_days += 7
        send_email(user, 'You have received 7 days of subscription as gift')


def send_ad(users: List[User]) -> None:
    """Envía un anuncio a los usuarios"""

    for user in users:
        send_email(user, 'This month, 50% off in all products')
