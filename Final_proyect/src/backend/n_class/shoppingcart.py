"""This file has the classes that represents the payment gategay of the plattform"""
from .catalogue import Catalogue
from .users import Customer
class Shoppingcart:
    """This class is a Shopping Cart """
    def __init__(self, id_, productslist, total) -> None:
        self.id_ = id_ 
        self.products = productslist
        self.total = total
        
