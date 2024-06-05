"""
To do: doc string
"""
from .users import Customer
class CreditCard:
    """This class represents a credit card"""

    def __init__(self, user_email:Customer , number: int, due_date: str, cvv: int, name: str):
        """
        Contructor of the class

        Parameters:

        - number(int): Number of the credit card.
        - due_data(str): Due data of the credit card.
        - cvv(int): Code cvv of the credit car  d.
        - name (str): Name of the credit card.
        
        """
        self.user_email = user_email
        self.number = number
        self.due_date = due_date
        self.cvv = cvv
        self.name = name
