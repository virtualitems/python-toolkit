# -*- coding: utf-8 -*-

"""
Function arguments lab
"""

def without_arguments():
    print('no arguments', end='\n\n\n')


def positional_arguments(arg1, arg2):
    print(f'positional arguments: {arg1}, {arg2}', end='\n\n\n')


def keyword_arguments(arg1, arg2):
    print(f'keyword arguments: {arg1}, {arg2}', end='\n\n\n')


def generic_arguments(*args, **kwargs):
    print(f'generic arguments: {args}, {kwargs}', end='\n\n\n')


def positional_only_arguments(arg1, arg2, **_):
    print(f'positional only arguments: {arg1}, {arg2}', end='\n\n\n')


def keyword_only_arguments(*_, arg1, arg2):
    print(f'keyword only arguments: {arg1}, {arg2}', end='\n\n\n')


def value_before_positional_generic(value, *args, **kwargs):
    print(f'value before positional generic: {value}, {args}, {kwargs}', end='\n\n\n')


def value_before_keyword_generic(*args, value, **kwargs):
    print(f'value between positional generic: {args}, {value}, {kwargs}', end='\n\n\n')


def main():

    without_arguments()

    positional_arguments('positional 1', 'positional 2')

    keyword_arguments(arg1='keyword 1', arg2='keyword 2')

    generic_arguments('generic 1', 'generic 2', arg1='kwgeneric 1', arg2='kwgeneric 2')

    positional_only_arguments('positional only 1', 'positional only 2', ignored='ignored')

    keyword_only_arguments('ignored', arg1='keyword only 1', arg2='keyword only 2')

    value_before_positional_generic('value', 'positional', keyword='keyword')

    value_before_keyword_generic('positional', value='value', keyword='keyword')


main()
