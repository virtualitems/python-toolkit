# -*- coding: utf-8 -*-

"""
docstring
"""

# standard library
from abc import ABC, abstractmethod
from collections.abc import Iterable


# ------------------------------
# Interfaces
# ------------------------------

class IRepositoryQuery(ABC):
    """
    docstring
    """

    @abstractmethod
    def resolve_expression(self, *args, **kwargs):
        """
        docstring
        """

    @abstractmethod
    def __and__(self, *args, **kwargs):
        """
        docstring &
        """

    @abstractmethod
    def __or__(self, *args, **kwargs):
        """
        docstring |
        """

    @abstractmethod
    def __invert__(self, *args, **kwargs):
        """
        docstring ~
        """


class IRepositoryResult(ABC, Iterable):
    """
    docstring
    """

    @abstractmethod
    def __init__(self, results):
        """
        docstring
        cached results
        """

    @abstractmethod
    def __iter__(self):
        """
        docstring
        """

    @abstractmethod
    def affected_count(self):
        """
        docstring
        """


class IDataView(ABC):
    """
    docstring
    returns primitives
    """

    @abstractmethod
    def all(self):
        """
        docstring
        """

    @abstractmethod
    def none(self):
        """
        docstring
        """


class IRepository(IDataView, ABC):
    """
    docstring
    returns entities
    """


class IFilterable(ABC):
    """
    docstring
    """

    @abstractmethod
    def filter(self, *args, **kwargs):
        """
        docstring
        """


class ICreateable(ABC):
    """
    docstring
    """

    @abstractmethod
    def create(self, *args, **kwargs):
        """
        docstring
        """


class IDeleteable(ABC):
    """
    docstring
    """

    @abstractmethod
    def delete(self, *args, **kwargs):
        """
        docstring
        """


class IUpdateable(ABC):
    """
    docstring
    """

    @abstractmethod
    def update(self, *args, **kwargs):
        """
        docstring
        """


class ITransactional(ABC):
    """
    docstring
    """

    @abstractmethod
    def begin_transaction(self, *args, **kwargs):
        """
        docstring
        """

    @abstractmethod
    def commit_transaction(self, *args, **kwargs):
        """
        docstring
        """

    @abstractmethod
    def rollback_transaction(self, *args, **kwargs):
        """
        docstring
        """


# ------------------------------
# Exceptions
# ------------------------------


class RepositoryException(Exception):
    """
    docstring
    """


class ResourceNotFoundException(RepositoryException):
    """
    docstring
    """


class ResourceAlreadyExistsException(RepositoryException):
    """
    docstring
    """
