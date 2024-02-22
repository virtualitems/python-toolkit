# -*- coding: utf-8 -*-

"""
Módulo de puertos
"""

# standard
from __future__ import annotations
from abc import ABCMeta, abstractmethod


class UserRepository(metaclass=ABCMeta):
    """
    Puerto para repositorios de usuarios.
    Un puerto es una interfaz que define un conjunto de operaciones que un adaptador debe implementar.
    (Port = Interface)
    """

    @abstractmethod
    def all(self):
        """Función para obtener todos los usuarios"""

    @abstractmethod
    def create(self, user):
        """Función para crear un usuario"""

    @abstractmethod
    def delete(self, user):
        """Función para eliminar un usuario"""
