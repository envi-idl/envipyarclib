"""
Defines the parameter template for the specified data type.
"""

from .basic import BASIC


class ULONG64(BASIC):
    """
    Defines the parameter template for the specified data type.
    """
    pass

def template():
    """Factory method for this parameter template class"""
    return ULONG64('GPLong')
