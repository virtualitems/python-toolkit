# -*- coding: utf-8 -*-

"""
docstring
"""

# standard library
from abc import ABC, abstractmethod
from collections.abc import Mapping


# ------------------------------
# Interfaces
# ------------------------------

class IDataTransferObject(ABC, Mapping):
    """
    docstring
    """

    @abstractmethod
    def is_valid(self, *args, **kwargs):
        """
        docstring
        """

    @abstractmethod
    def __getitem__(self, key):
        """
        docstring
        """

    @abstractmethod
    def __iter__(self):
        """
        docstring
        """

    @abstractmethod
    def __len__(self):
        """
        docstring
        """


class ISerializer(ABC):
    """
    docstring
    many >-to-> one
    """

    @abstractmethod
    def serialize(self, *args, **kwargs):
        """
        docstring
        """
