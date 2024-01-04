# -*- coding: utf-8 -*-

"""
docstring
"""

# standard library
from abc import ABC, abstractmethod
from collections import namedtuple


# ------------------------------
# Bases
# ------------------------------

ImmutableValue = namedtuple('ImmutableValue', ('value',))


# ------------------------------
# Interfaces
# ------------------------------

class ValueObject(ABC, ImmutableValue):
    """
    docstring
    """

    def __init__(self, value):

        if not self.is_valid(value):
            raise ValueError(f'{value} is not a valid value for {self.__class__.__name__}')

    def __str__(self):
        return str(self.value)

    @abstractmethod
    def is_valid(self, value):
        """
        Checks if the value is valid for this value object.
        """
