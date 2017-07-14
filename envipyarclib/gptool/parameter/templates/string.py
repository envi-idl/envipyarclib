"""
Defines the parameter template for the specified data type.
"""
from __future__ import absolute_import
from string import Template
from .basic import BASIC



class STRING(BASIC):
    """
    Defines the parameter template for the specified data type.
    """

    def default_value(self):
        return Template('''
        ${name}.value = "$defaultValue"
''')

def template():
    """Factory method for this parameter template class"""
    return STRING('GPString')
