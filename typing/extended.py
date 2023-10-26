# -*- coding: utf-8 -*-

"""
typing library extension
"""

# standard library

from typing import (
    Any,
    Callable,
    Dict,
    FrozenSet,
    List,
    Set,
    Tuple,
    Type,
    Union,
)


# python based types

Unknown = Union[None, Any]

Binary = Union[bytes, bytearray, memoryview]

Numeric = Union[int, bool, float, complex]

Primitive = Union[bytes, int, bool]

Alphanumeric = Union[Numeric, str]

Basic = Union[Binary, Alphanumeric]

Native = Union[Basic, range, List, Tuple, Dict, Set, FrozenSet]

ImmutableSequence = Union[bytes, str, range, Tuple, FrozenSet]

Never = Type[None]


# concept based types

Serializable = Union[int, bool, float, str, List, Tuple, Dict]

Json = Union[Dict[str, Serializable], List[Serializable], Tuple[Serializable]]

Getter = Callable[[], Any]

Setter = Callable[[Any], Unknown]


# all list

__all__ = [
    'Unknown',
    'Binary',
    'Numeric',
    'Primitive',
    'Alphanumeric',
    'Basic',
    'Native',
    'ImmutableSequence',
    'Never',
    'Serializable',
    'Json',
    'Getter',
    'Setter',
]
