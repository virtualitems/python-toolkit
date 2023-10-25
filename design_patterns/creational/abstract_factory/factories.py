"""
Módulo de fábricas
"""


from __future__ import annotations

from abc import ABC, abstractmethod

from products import (
    Chair, Table,
    VictorianChair, VictorianTable,
    ModernChair, ModernTable,
)


class AbstractFactory(ABC):
    """
    El objetivo del AbstractFactory es definir los métodos
    que se implementarán en las fábricas.
    El AbstractFactory debe contener métodos para crear
    las abstracciones de los distintos productos de cada familia.
    """
    @abstractmethod
    def create_chair(self) -> Chair:
        """
        Crea un silla
        """

    @abstractmethod
    def create_table(self) -> Table:
        """
        Crea una mesa
        """

class VictorianFactory(AbstractFactory):
    """
    Fábrica para crar productos del tipo Victoriano.
    """

    def create_chair(self) -> Chair:
        return VictorianChair()

    def create_table(self) -> Table:
        return VictorianTable()


class ModernFactory(AbstractFactory):
    """
    Fábrica para crar productos del tipo Moderno.
    """

    def create_chair(self) -> Chair:
        return ModernChair()

    def create_table(self) -> Table:
        return ModernTable()