# -*- coding: utf-8 -*-

"""
docstring
"""

# standard library
from abc import ABC, abstractmethod


# ------------------------------
# Interfaces
# ------------------------------

class IRandomGenerator(ABC):
    """
    docstring
    """

    @abstractmethod
    def generate(self, *args, **kwargs):
        """
        docstring
        """
