"""
To do: doc string
"""
from pydantic import BaseModel

class CreditCard(BaseModel):
    """This class represents a credit card"""
    customer_username: str
    number: str
    due_date: str
    cvv: int
    name: str
