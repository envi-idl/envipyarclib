"""
Defines the Bool array parameter template
"""

from .basicarray import BASICARRAY


class BOOLARRAY(BASICARRAY):
    """
    Defines the Bool array parameter template
    """
    pass


def template():
    """Factory method for this parameter template class"""
    return BOOLARRAY('GPBoolean')
