"""
Defines the parameter template for the specified data type.
"""
from .enviuri import ENVIURI

class ENVIVIRTUALIZABLEURI(ENVIURI):
    def __init__(self, data_type):
        super(ENVIURI, self).__init__(data_type)

def template():
    """Factory method for this parameter template class"""
    return ENVIVIRTUALIZABLEURI('DEFile')

