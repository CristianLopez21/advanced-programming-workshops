""" To do: docstring"""
from pydantic import BaseModel
from typing import Optional

class Shoppinghistory(BaseModel):
    """This class represents"""
    id: int
    date: str
    products: list
    total: float

class User(BaseModel):
    """This class represents a basemodel of the user that can be use the platform"""
    id_: int = None
    user_name: str
    password: str
    user_email: str
    phone: str
    access: bool = None

    @staticmethod
    def login(user_email: str, password: str):
        """This methood make all the process for validate the credentials of the users"""
        return User(id_= "A1", user_name= "name",phone = "phone", user_email= user_email, password = password, access = "access")

# -------------------Custumer---------------------------
class Customer(User):
    """This class represents the external users that buy in the platform"""

    address: Optional[str] = None
    shoppinghistory: Optional[Shoppinghistory] = None

    def add_shipping_address(self, user_email: str):
        """This method is used to add a shipping adress for the user
        Parameters:

        - user_email
        """
        self.shipping_address[user_email] = input("Enter your shipping addres")
        #TODO save on a data base

    @classmethod
    def show_history(cls, user_email):
        """This method is used to show the history of the user in the platfform"""
        return cls.shopping_history.get(user_email, [])

#----------------------------Administrador_____________
class Admin(User):
    """This class represents the users that can add new products to the platform"""


class UserCredentials(BaseModel):
    """This class represents idk this was doing by Carlos"""
    user_email: str
    password: str
