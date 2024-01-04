# -*- coding: utf-8 -*-

"""
docstring
"""


# ------------------------------
# Singletons
# ------------------------------

class SingletonMeta(type):
    """
    Singleton Metaclass
    """

    instance = None

    def __call__(cls, *args, **kwargs):

        if cls.instance is None:
            cls.instance = super().__call__(*args, **kwargs)

        return cls.instance


class ConfigurationsDict(dict, metaclass=SingletonMeta):
    """
    docstring
    """
