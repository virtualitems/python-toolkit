# -*- coding: utf-8 -*-

"""
docstring
"""

# standard library
from abc import ABC, abstractmethod


# ------------------------------
# Interfaces
# ------------------------------

class ISignal(ABC):
    """
    docstring
    """

    @abstractmethod
    def get_type(self, *args, **kwargs):
        """
        docstring
        """

    @abstractmethod
    def get_details(self, *args, **kwargs):
        """
        docstring
        """


class ISignalBus(ABC):
    """
    docstring
    """

    @abstractmethod
    def subscribe(self, *args, **kwargs):
        """
        docstring
        """

    @abstractmethod
    def unsubscribe(self, *args, **kwargs):
        """
        docstring
        """

    @abstractmethod
    def publish(self, *args, **kwargs):
        """
        docstring
        """


class ISignalHandler(ABC):
    """
    docstring
    """

    @abstractmethod
    def handle(self, *args, **kwargs):
        """
        docstring
        """
