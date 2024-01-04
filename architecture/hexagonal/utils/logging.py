# -*- coding: utf-8 -*-

"""
docstring
"""

# standard library
from abc import ABC, abstractmethod


# ------------------------------
# Interfaces
# ------------------------------

class IMessageLogger(ABC):
    """
    docstring
    """

    @abstractmethod
    def debug(self, *args, **kwargs):
        """
        docstring
        """

    @abstractmethod
    def info(self, *args, **kwargs):
        """
        docstring
        """

    @abstractmethod
    def warning(self, *args, **kwargs):
        """
        docstring
        """

    @abstractmethod
    def error(self, *args, **kwargs):
        """
        docstring
        """

    @abstractmethod
    def critical(self, *args, **kwargs):
        """
        docstring
        """


class IRepresenterLogger(ABC):
    """
    docstring
    """

    @abstractmethod
    def __repr__(self):
        """
        docstring
        """


class IContextLogger(ABC):
    """
    docstring
    """

    @abstractmethod
    def __enter__(self, *args, **kwargs):
        """
        docstring
        """

    @abstractmethod
    def __exit__(self, *args, **kwargs):
        """
        docstring
        """
