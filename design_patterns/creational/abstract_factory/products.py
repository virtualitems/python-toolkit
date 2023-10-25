"""
Módulo de productos y familias de productos.
"""


from __future__ import annotations

from abc import ABC, abstractmethod


#--------------------
# Silla
#--------------------

class Chair(ABC):
    """
    Abstracción para las sillas.
    """

    @abstractmethod
    def be_awesome(self) -> str:
        """
        Una silla asombrosa
        """

class VictorianChair(Chair):
    """
    Implementación para las sillas del tipo Victoriano.
    """
    def be_awesome(self) -> str:
        return '¡La silla victoriana es asombrosa!'


class ModernChair(Chair):
    """
    Implementación para las sillas del tipo Moderno.
    """
    def be_awesome(self) -> str:
        return '¡La silla moderna es asombrosa!'


#--------------------
# Mesa
#--------------------

class Table(ABC):
    """
    Abstracción para las mesas.
    """

    @abstractmethod
    def be_awesome(self) -> str:
        """
        Una mesa asombrosa
        """

    def be_awesome_with_chair(self, chair: Chair) -> str:
        """
        Una mesa puede usar una silla.
        """
        return f'{self.be_awesome()} y también {chair.be_awesome()}'



class VictorianTable(Table):
    """
    Implementación para las mesas del tipo Victoriano.
    """
    def be_awesome(self) -> str:
        return '¡La mesa victoriana es asombrosa!'


class ModernTable(Table):
    """
    Implementación para las mesas del tipo Moderno.
    """
    def be_awesome(self) -> str:
        return '¡La mesa moderna es asombrosa!'
