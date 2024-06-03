"""
To do: doc string
"""
from pydantic import BaseModel
class CreditCard(BaseModel):
    """This class represents a credit card"""
    
    user_email : str
    number : str
    due_date : str
    cvv : str
    name : str
    
    """
    T  This class represents a credit card
        
    """
