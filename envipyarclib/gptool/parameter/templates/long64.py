"""
Defines the parameter template for the specified data type.
"""

from .basic import BASIC


class LONG64(BASIC):
    """
    Defines the parameter template for the specified data type.
    """
    pass

def template():
    """Factory method for this parameter template class"""
    return LONG64('GPLong')
