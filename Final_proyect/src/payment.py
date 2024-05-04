"""This file has the classes that represents the payment gategay of the plattform"""
from catalogue_basemodel import Catalogue
from users_basemodel import Customer
class PaymentGateway:
    """This class is a Payment gateway """
    def __init__(self) -> None:
        self.login_status = None

    def buy_product(self, code):
        """This method do the process to pay a product"""
        product = Catalogue.get_product(code)
        Customer.shoping_history.append(product)