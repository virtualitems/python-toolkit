# -*- coding: utf-8 -*-

"""
Implementación del patrón Singleton
"""

# standard
from __future__ import annotations
from typing import TYPE_CHECKING

# first-party
from singleton import SingletonBaseClass

# typing
if TYPE_CHECKING:  # pragma: no cover
    from typing import Any


class Singleton(SingletonBaseClass):
    """
    Clase que implementa el patrón Singleton
    """
    value: Any

    def __init__(self, value) -> None:
        """
        Inicializador de la clase.
        Debido a que es un Singleton, sólo se ejecuta una vez.
        """
        self.value = value


def main():
    """Función principal"""

    singleton_one = Singleton(2)
    singleton_two = Singleton(4)

    print(f'same reference: {singleton_one is singleton_two}')

    print(f'first: {singleton_one.value}')
    print(f'second: {singleton_two.value}')

    singleton_two.value = 6

    print('after change')
    print(f'first: {singleton_one.value}')
    print(f'second: {singleton_two.value}')


if __name__ == "__main__":
    main()
