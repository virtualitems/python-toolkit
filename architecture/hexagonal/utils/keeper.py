# -*- coding: utf-8 -*-

"""
docstring
"""

# standard library
from abc import ABC, abstractmethod


# ------------------------------
# Interfaces
# ------------------------------

class IDataKeeper(ABC, dict):
    """
    docstring
    """

    @abstractmethod
    def __setitem__(self, key, value):
        """
        docstring
        """


class IDataSpace(ABC, list):
    """
    docstring
    """

    @abstractmethod
    def __setitem__(self, key, value):
        """
        docstring
        """
