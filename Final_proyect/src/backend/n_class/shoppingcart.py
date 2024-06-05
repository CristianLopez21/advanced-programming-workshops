"""This file has the classes that represents the payment gategay of the plattform"""
from .catalogue import Catalogue
from .users import Customer
class Shoppingcart:
    """This class is a Shopping Cart """
    def __init__(self) -> None:
        pass
        
    def buy_product(self, code):
        """This method do the process to pay a product"""
        product = Catalogue.get_product(code)
        Customer.shoping_history.append(product)
