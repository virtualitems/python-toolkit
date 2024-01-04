# -*- coding: utf-8 -*-

"""
docstring
"""

# standard library
from abc import ABC, abstractmethod


# ------------------------------
# Interfaces
# ------------------------------

class IEntity(ABC):
    """
    docstring
    """

    @abstractmethod
    def __eq__(self, *args, **kwargs):
        """
        docstring
        """


class IAgregate(IEntity, ABC):
    """
    docstring
    """
