# -*- coding: utf-8 -*-

"""
docstring
"""

# standard
from __future__ import annotations
from typing import TYPE_CHECKING
from dataclasses import dataclass

# framework

# third-party

# first-party

# typing
if TYPE_CHECKING:  # pragma: no cover
    pass


@dataclass
class User:
    """Modelo de datos que describe a un usuario"""
    id: str = None
    name: str = None
