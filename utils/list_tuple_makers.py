# -*- coding: utf-8 -*-

"""
Python standard library aditional utils
"""

from typing import TYPE_CHECKING


if TYPE_CHECKING:  # pragma: no cover
    from typing import List, Tuple


def make_tuple(*args) -> 'Tuple':
    """Build and returns a tuple object.

    Args:
        args: positional arguments

    Returns:
        the tuple object
    """
    args_length = len(args)

    if args_length == 0:
        return tuple()

    if args_length == 1 and hasattr(args[0], '__iter__'):
        return tuple(args[0])

    return tuple(args)


def make_list(*args) -> 'List':
    """Build and returns a list object.

    Args:
        args: positional arguments

    Returns:
        the list object
    """

    args_length = len(args)

    if args_length == 0:
        return []

    if args_length == 1 and hasattr(args[0], '__iter__'):
        return list(args[0])

    return list(args)
