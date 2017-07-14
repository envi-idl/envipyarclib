"""
Defines the parameter template for the specified data type.
"""
from .basic import BASIC


class BOOLEAN(BASIC):
    """
    Defines the parameter template for the specified data type.
    """
    pass

def template():
    """Factory method for this parameter template class"""
    return BOOLEAN('GPBoolean')
