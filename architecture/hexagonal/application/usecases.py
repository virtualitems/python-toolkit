# -*- coding: utf-8 -*-

"""
docstring
"""

# standard library
from abc import ABC, abstractmethod


# ------------------------------
# Interfaces
# ------------------------------

class Command(ABC):
    """
    docstring
    """


class Query(ABC):
    """
    docstring
    """


class IUseCaseRequest(ABC):
    """
    docstring
    """

    @abstractmethod
    def get_queries(self, *args, **kwargs):
        """
        docstring
        """

    @abstractmethod
    def get_commands(self, *args, **kwargs):
        """
        docstring
        """

    @abstractmethod
    def get_details(self, *args, **kwargs):
        """
        docstring
        """


class IUseCaseResponse(ABC):
    """
    docstring
    """

    @abstractmethod
    def get_message(self, *args, **kwargs):
        """
        docstring
        """

    @abstractmethod
    def get_data(self, *args, **kwargs):
        """
        docstring
        """

    @abstractmethod
    def get_error(self, *args, **kwargs):
        """
        docstring
        """


class IUseCase(ABC):
    """
    docstring
    """

    @abstractmethod
    def resolve(self, *args, **kwargs):
        """
        docstring
        """


# ------------------------------
# Exceptions
# ------------------------------

class UseCaseException(Exception):
    """
    docstring
    """
