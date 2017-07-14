"""
Defines the parameter template for the specified data type.
"""
from .basicarray import BASICARRAY


class STRINGARRAY(BASICARRAY):
    """
    Defines the parameter template for the specified data type.
    """
    pass


def template():
    """Factory method for this parameter template class"""
    return STRINGARRAY('GPString')
