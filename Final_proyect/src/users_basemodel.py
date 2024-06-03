from pydantic import BaseModel
from catalogue import Catalogue
from product_basemodel import Product
from credit_card import CreditCard

#from credit_card import CreditCard
#Dictionaries
custumers = {}
admins = {}
paymethods = {}
products = {}



class User(BaseModel):
    """This class represents a basemodel of the user that can be use the platform"""
    user_name: str
    phone: str
    user_email: str
    password: str
    access: str

    @staticmethod
    def login(user_email: str, password:str):
        """This method make all the process for validate the credentials of the users"""
        return User(user_name= "name",phone = "phone", user_email= user_email, password = password, access = "access")

    
        

   

# -------------------Customer---------------------------
class Customer(User):
    """This class represents the external users that buy in the platform"""

    def __init__(self, user_name: str, phone: str, user_email: str, password: str, access: bool, shipping_address, shopping_history : list, credit_card: CreditCard):
        """
        Contructor of the class

        Parameters:

        - user_name (str): Name of the customer.
        - phone (str): Phone of the customer.
        - user_email(str): Email of the customer.
        - password(str): Password of the customer.
        - shipping_adress(str): Shipping adress of the customer.
        - pay_ method(str): Pay method of the customer.
        """
        super().__init__(user_name= user_name, phone=phone, user_email= user_email, password=password, access= access)
        self.shipping_address = shipping_address
        self.shopping_history = shopping_history

    
    
    @classmethod
    def show_history(cls, user_email):
        """This method is used to show the history of the user in the platfform"""
        return cls.shopping_history.get(user_email, [])

#----------------------------Admin_____________
class Admin(User):
    """This class represents the users that can add new products to the platform"""
    def __init__(self, user_name: str, phone: str, user_email: str, password:
                 str, access: bool):
        super().__init__(user_name=user_name, phone=phone, user_email=user_email, password=password, access=access)

    def add_product(self, access, product: Product):
        """This method validate that the user have the permission, 
        if they have permission, can add products"""
       
        if self.access == "True":
            return Catalogue.add_product(product)
        else:
            return False


    def test_admins_integrity(self):
        """This function test that the costumer was saved on the dictionary"""
        for user_email,admin in admins.items():
            print(f"Usermail: {user_email}, Password: {admin.password}, username: {admin.user_name}, phone: {admin.phone}, Acces: {admin.access}.")