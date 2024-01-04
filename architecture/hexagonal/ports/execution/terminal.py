# -*- coding: utf-8 -*-

"""
docstring
"""

# standard library
from abc import ABC, abstractmethod


# ------------------------------
# Interfaces
# ------------------------------

class ITerminalAdapter(ABC):
    """
    docstring
    """

    @abstractmethod
    def execute(self, *args, **kwargs):
        """
        docstring
        """
