"""
Defines the parameter template for the specified data type.
"""
from .enviuriarray import ENVIURIARRAY

class ENVIVIRTUALIZABLEURIARRAY(ENVIURIARRAY):
    def __init__(self, data_type):
        super(ENVIURIARRAY, self).__init__(data_type)

def template():
    """Factory method for this parameter template class"""
    return ENVIVIRTUALIZABLEURIARRAY('DEFile')

