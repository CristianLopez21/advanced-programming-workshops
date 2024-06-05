""""This file has the classes that represent the users who can use the online sales platform"""
from .credit_card import CreditCard
#Dictionaries
users = {}
paymethods = {}

class User:
    """This class represents the user that can be use the platform"""

    def __init__(self, user_email: str, password: str, user_name: str, phone: str, access: bool):
        """ 
        Constructor of the class

        Parameters:
        - user_name (str): Name of the user.
        - phone (str): Phone of the user
        - user_email(str): Email of the user.
        - password(str): Password of the user.
        - access(bool): It is the permission that allows access to certain functions
        """
        self.user_email = user_email
        self.password = password
        self.user_name = user_name
        self.phone = phone
        self.access = access

    def login(self,user_email, password):
        """This methood make all the process for validate the credentials of the users"""
        if user_email == self.user_email and  password == self.password:
            return User(user_name= "name",phone = "phone", user_email= user_email, password = password, access = "access")
        else:
            return False

    @staticmethod
    def create_customer(user_email, password, user_name, phone, access):
        """This method create the object Customer and save in the database"""
        
        # TODO save on data base meanwhile it will be saved to a dictionary
        new_costumer = Customer(user_email, password, user_name, phone, access)
        users[user_email] = new_costumer

    @staticmethod
    def create_admin(user_email,password,user_name,phone,access):
        """This method create the object Admin and save in the database"""

        # TODO save on data base meanwhile it will be saved to a dictionary
        new_admin = Admin(user_email,password,user_name,phone,access)
        users[user_email] = new_admin

# -------------------Custumer---------------------------
class Customer(User):
    """This class represents the external users that buy in the platform"""

    def __init__(self, user_email: str, password: str, user_name: str, phone: str, access: bool):
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
        super().__init__(user_email, password, user_name, phone, access)
        self.shipping_address = {}
        self.shoping_history = []

    def add_shipping_address(self, user_email: str):
        """This method is used to add a shipping adress for the user
        Parameters:

        - user_email
        """
        self.shipping_address[user_email] = input("Enter your shipping addres")
        #TODO save on a data base

    def add_pay_method(self, user_email: str, number, due_date, cvv, name):
        """This method is used to add a pay method for the user"""

        new_creditcard = CreditCard(user_email, number, due_date, cvv, name)
        paymethods[user_email] = new_creditcard

    def show_history(self):
        """This method is used to show the history of the user in the platfform"""

#----------------------------Administrador_____________
class Admin(User):
    """This class represents the users that can add new products to the platform"""
    def __init__(self, user_email: str, password: str, user_name: str,
                 phone: str,  access: bool):
        super().__init__(user_email, password, user_name, phone, access)

    def add_product(self, access):
        """This method validate that the user have the permission, 
        if they have permission, can add products"""

        if access == True:
            pass
         
    def test_admins_integrity(self):
        """This function test that the costumer was saved on the dictionary"""
        for user_email,admin in users.items():
            print(f"Usermail: {user_email}, Password: {admin.password}, username: {admin.user_name}, phone: {admin.phone}, Acces: {admin.access}.")
