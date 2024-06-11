""" To do: docstring"""
from pydantic import BaseModel
from typing import Optional
from credit_card_bm import CreditCard
from shoppingcart import Shoppingcart

class Shoppinghistory(BaseModel):
    """This class represents"""
    date: str
    purchasedprod: Shoppingcart

class User(BaseModel):
    """This class represents a basemodel of the user that can be use the platform"""
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
    """This class represents the external users that buy in the platform"""

    address: Optional[str] = None
    shoppinghistory: Optional[Shoppinghistory] = None
    pay_methods: Optional[CreditCard] = None
    class Config:
        protected_namespaces = ()

#----------------------------Administrador_____________
class Admin(User):
    """This class represents the users that can add new products to the platform"""
    class Config:
        protected_namespaces = ()

class UserCredentials(BaseModel):
    """This class represents idk this was doing by Carlos"""
    user_email: str
    password: str
