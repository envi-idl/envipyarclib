"""
Defines the parameter template for the specified data type.
"""
from .basic import BASIC


class UINT(BASIC):
    """
    Defines the parameter template for the specified data type.
    """
    pass


def template():
    """Factory method for this parameter template class"""
    return UINT('GPLong')
