""""IDK"""


class User:
    """This class represents the users that can be use the platform"""

    def __init__(self, user_name: str, phone: str, user_email: str, password: str):
        self.user_name = user_name
        self.phone = phone
        self.user_email = user_email
        self.password = password
        self.acces = {}

    def login(self):
        """This methood make all the process for validate the credentials of the users"""

    def create_account(self):
        """This method create the object user and save in the database"""

    def add_product(self, acces):
        """This method validate that the user have the permission, 
        if they have permission, can add products"""
        # if acces == True:


# -------------------Costumer---------------------------
class Costumer(User):
    """This class represents the external users that buy in the platform"""

    def __init__(self, user_name: str, phone: str, user_email: str, password: str):
        super().__init__(user_name, phone, user_email, password)
        self.shipping_address = {}
        self.pay_method = {}
        self.shoping_history = {}

    def add_shipping_address(self):
        """This method"""

    def add_pay_method(self):
        """This method"""

    def show_history(self):
        """This method"""


# --------------------Admin---------------------------


# -------------------Credit cart--------------------------
class Creditcard:
    """This class represents a credit card"""

    def __init__(self, number: int, due_date: str, cvv: int, name: str):
        self.number = number
        self.due_date = due_date
        self.cvv = cvv
        self.name = name
