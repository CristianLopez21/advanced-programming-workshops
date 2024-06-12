""" This file stores all the models(classes) used to define the different users
 of the application and the elements that interact with this"""

from pydantic import BaseModel
from typing import Optional
from credit_card_bm import CreditCard

class Shoppingcart(BaseModel):
    """This class represents a user's shopping cart.

        Attributes:
        - id_ (int): The unique identifier of the purchase being made
        - products (list): A list of the products purchased in this purchase.
        - total (float): The total cost of the products in this purchase
    """
    id_: int = None
    products: list
    total: float

class Shoppinghistory(BaseModel):
    """ 
    This class represents a user's purchase history.

    Attributes:
    - date (string): When the purchase activity occurred.
    - compraprod (Shoppingcart): the Shoppingcart class provides us with an ID to identify the purchase,
      the products purchased in this purchase, and the total price paid in this purchase.
    """
    date: str
    purchasedprod: Shoppingcart

class User(BaseModel):
    """ This class represents a base model of the user that can use the platform.

        Attributes:
        - id_ (Optional[int]): The unique identifier of the user. Defaults to None.
        - user_name (str): The username of the user.
        - password (str): The password of the user.
        - user_email (str): The email address of the user.
        - phone (str): The phone number of the user.
        - access (Optional[bool]): Indicates whether the user has access. Defaults to None.
        
    """
    id_: Optional[int] = None
    user_name: str
    password: str
    user_email: str
    phone: str
    access: Optional[bool] = None
    class Config:
        protected_namespaces = ()

# -------------------Custumer---------------------------
class Customer(User):
    """This class represents the external users that buy on the platform.

       Inherits from: 
       - User: The base user class with common attributes such as user_name, password, user_email, phone, and access.

        Attributes:
        - address (Optional[str]): The address of the customer. Defaults to None.
        - shoppinghistory (Optional[Shoppinghistory]): The shopping history of the customer. Defaults to None.
        - pay_methods (Optional[CreditCard]): The payment methods associated with the customer. Defaults to None.
    """

    address: Optional[str] = None
    shoppinghistory: Optional[Shoppinghistory] = None
    pay_methods: Optional[CreditCard] = None

#----------------------------Administrador_____________
class Admin(User):
    """This class represents the users that can add new products to the platform.

       Inherits from:
       - User: The base user class with common attributes such as user_name, password, user_email, phone, and access.
    """
    class Config:
        protected_namespaces = ()

class UserCredentials(BaseModel):
    """This class represents the credentials used to validate the identity of the user.

        Attributes:
        - user_email (str): The email address of the user.
        - password (str): The password of the user.
    """
    user_email: str
    password: str
