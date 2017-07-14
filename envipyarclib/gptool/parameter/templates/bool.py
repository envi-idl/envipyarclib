"""
Defines the Bool parameter template
"""
from .basic import BASIC


class BOOL(BASIC):
    """
    Defines the Bool parameter template
    """
    pass

def template():
    """Factory method for this parameter template class"""
    return BOOL('GPBoolean')
