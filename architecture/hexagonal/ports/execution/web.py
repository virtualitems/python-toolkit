# -*- coding: utf-8 -*-

"""
docstring
"""

# standard library
from abc import ABC, abstractmethod


# ------------------------------
# Interfaces
# ------------------------------

class IWebAdapter(ABC):
    """
    docstring
    """

    @abstractmethod
    def head(self, *args, **kwargs):
        """
        docstring
        """

    @abstractmethod
    def options(self, *args, **kwargs):
        """
        docstring
        """

    @abstractmethod
    def get(self, *args, **kwargs):
        """
        docstring
        """

    @abstractmethod
    def post(self, *args, **kwargs):
        """
        docstring
        """

    @abstractmethod
    def put(self, *args, **kwargs):
        """
        docstring
        """

    @abstractmethod
    def patch(self, *args, **kwargs):
        """
        docstring
        """

    @abstractmethod
    def delete(self, *args, **kwargs):
        """
        docstring
        """
