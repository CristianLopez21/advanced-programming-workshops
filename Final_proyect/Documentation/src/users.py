""""This file has the classes that represent the users who can use the online sales platform"""


class User:
    """This class represents the user that can be use the platform"""

    def __init__(self, user_name: str, phone: str, user_email: str, password: str):
        """ 
        Constructor of the class

        Parameters:
        - user_name (str): Name of the user.
        - phone (str): Phone of the user
        - user_email(str): Email of the user.
        - password(str): Password of the user.

        """


        
        self.user_name = user_name
        self.phone = phone
        self.user_email = user_email
        self.password = password
        self.access = {}

    def login(self, email, password):
        """This methood make all the process for validate the credentials of the users"""
        if email== self.user_email and  password == self.password:
            return True
        else: 
            return False


    def create_account(self, user_name, phone,  user_email, password):
        """This method create the object user and save in the database"""
        self.user_name = user_name
        self.phone = phone
        self.user_email = user_email
        self.password = password
        

    def add_product(self, email, password):
        """This method validate that the user have the permission, 
        if they have permission, can add products"""
       

        # if acces == True:


# -------------------Costumer---------------------------
class Customer(User):
    """This class represents the external users that buy in the platform"""

    def __init__(self, user_name: str, phone: str, user_email: str, password: str, shipping_adress: str, pay_method : str ):
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
        super().__init__(user_name, phone, user_email, password)
        self.shipping_address = {}
        self.pay_method = {}
        self.shoping_history = {}

    def add_shipping_address(self, shipping_adress):
        """This method is used to add a shipping adress for the user
        Parameters:
        - shipping

        """
        self.shipping_address= shipping_adress

        

    def add_pay_method(self):
        """This method is used to add a pay method for the user """

    def show_history(self):
        """This method is used to show the history of the user in the platfform"""


# --------------------Admin---------------------------
class Admin (User):
    """This class represents Admin of the plattform"""

    def __init__(self, user_name: str, phone: str, user_email: str, password: str ):
        """
        Contructor of the class

        Parameters:

        - user_name (str): Name of the Amin.
        - phone (str): Phone of the Admin.
        - user_email(str): Email of the Admin.
        - password(str): Password of the Admin.
        

        
        
        """
        super().__init__(user_name, phone, user_email, password)
        

   

# -------------------Credit cart--------------------------
class CreditCard:
    """This class represents a credit card"""

    def __init__(self, number: int, due_date: str, cvv: int, name: str):
        """
        Contructor of the class

        Parameters:

        - number(int): Number of the credit card.
        - due_data(str): Due data of the credit card.
        - cvv(int): Code cvv of the credit card.
        - name (str): Name of the credit card.
        
        """
        self.number = number
        self.due_date = due_date
        self.cvv = cvv
        self.name = name
