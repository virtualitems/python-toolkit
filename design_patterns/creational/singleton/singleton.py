# -*- coding: utf-8 -*-

"""
Módulo de definición para el patrón Singleton
"""

# standard
from __future__ import annotations
from builtins import type
from typing import TYPE_CHECKING

# typing
if TYPE_CHECKING:  # pragma: no cover
    pass


class MetaSingleton(type):
    """
    Al definir la clase Meta para el patrón Singleton,
    se puede controlar la creación de instancias de la clase.
    """

    _instances = {}

    def __call__(cls, *args, **kwargs):
        """
        Al llamar a la clase, se verifica si existe una instancia.
        Si no existe, se crea una nueva instancia.
        Pero esto sólo se hace la primera vez que se llama a la clase.
        """
        if cls not in cls._instances:
            instance = super().__call__(*args, **kwargs)
            cls._instances[cls] = instance

        return cls._instances[cls]


class SingletonBaseClass(metaclass=MetaSingleton):
    """
    Clase base para el patrón Singleton
    """
