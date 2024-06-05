"""
To do: doc string
"""
from pydantic import BaseModel
from .users_basemodel import Customer

class CreditCard(BaseModel):
    """This class represents a credit card"""

    user_email = Customer
    number = str
    due_date = str
    cvv = int
    name = str
