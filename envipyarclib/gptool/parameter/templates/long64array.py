"""
Defines the parameter template for the specified data type.
"""

from .basicarray import BASICARRAY


class LONG64ARRAY(BASICARRAY):
    """
    Defines the parameter template for the specified data type.
    """
    pass

def template():
    """Factory method for this parameter template class"""
    return LONG64ARRAY('GPLong')
