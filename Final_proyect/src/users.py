""""This file has the classes that represent the users who can use the online sales platform"""
from catalogue import Catalogue
from product import Product
#Dictionaries
customers = {}
admins = {}
pay_method = {}
class User:
    """This class represents the user that can be use the platform"""

    def __init__(self, user_name: str, phone: str, user_email: str, password: str, access: bool):
        """ 
        Constructor of the class

        Parameters:
        - user_name (str): Name of the user.
        - phone (str): Phone of the user
        - user_email(str): Email of the user.
        - password(str): Password of the user.
        - access(bool): It is the permission that allows access to certain functions
        """
        self.user_name = user_name
        self.phone = phone
        self.user_email = user_email
        self.password = password
        self.access = access

    def login(self,user_email, password):
        """This methood make all the process for validate the credentials of the users"""
        if user_email == self.user_email and  password == self.password:
            return True
        else:
            return False

    @staticmethod
    def create_account():
        """This method create the object user and save in the database"""
        type_user = int(input("Seleccione el tipo de ususario: 1. Cliente 2. Admin: "))
        if type_user == 1:
            access = False
            user_email = input("Email: ")
            password = input("Password: ")
            user_name = input("User name: ")
            phone = input("Phone number: ")
            # TODO save on data base meanwhile it will be saved to a dictionary
            new_costumer = Customer(user_name,phone, user_email,password,access)
            customers[user_email] = new_costumer
        elif type_user == 2:
            access = True
            user_email = input("Email: ")
            password = input("Password: ")
            user_name = input("User name: ")
            phone = input("Phone number: ")
            # TODO save on data base meanwhile it will be saved to a dictionary
            new_admin = Admin(user_name,phone,user_email,password,access)
            admins[user_email] = new_admin

        else:
            raise ValueError("The option enteerd does not exist, please try again. ")

# -------------------Costumer---------------------------
   
class Customer(User):
    """This class represents the external users that buy in the platform"""

    def __init__(self, user_name: str, phone: str, user_email: str, password: str, access: bool):
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
        super().__init__(user_name, phone, user_email, password, access)
        self.shipping_address = {}
        self.shoping_history = {}

    def add_shipping_address(self, user_email: str):
        """This method is used to add a shipping adress for the user
        Parameters:

        - user_email
        """
        self.shipping_address[user_email] = input("Enter your shipping addres")
        #TODO save on a data base

    def add_pay_method(self, user_email: str):
        """This method is used to add a pay method for the user"""

        from credit_card import CreditCard
        number = input("Enter the number of the credit card")
        due_date = input("Enter the due date that appear in the credit card")
        cvv = input("Enter the cvv code that appear in the credit card")
        name = input("Enter the name that appear in the credit card")
        new_creditcard = CreditCard(user_email, number, due_date, cvv, name)
        for user_email in customers.items():
            pay_method[user_email] = new_creditcard
            #This prints were used to validate that the data have the correct type
            # and data that was entered
            print(type(new_creditcard))
            print(f"UserMail: {user_email}, NUMBER: {number}, DUE_DATE: {due_date}, CVV: {cvv}, NAME: {name}")

    def show_history(self):
        """This method is used to show the history of the user in the platfform"""

    def test_costumers_integrity(self):
        """This function test that the costumer was saved on the dictionary"""
        for user_email,customer in customers.items():
            print(f"Usermail: {user_email}, Password: {customer.password}, username: {customer.user_name}, phone: {customer.phone}, Acces: {customer.access}.")
            return user_email
        

    def buy_product(self):
        """This method is used to buy a product"""

#----------------------------Admin_____________
class Admin(User):
    """This class represents the users that can add new products to the platform"""
    
    def __init__(self, user_name: str, phone: str, user_email: str, password:
                 str, access: bool):
        super().__init__(user_name, phone, user_email, password, access)
    
    
    def add_product(self, access:bool, product:Product):
        """This method validate that the user have the permission, 
        if they have permission, can add products"""
        if access == self.access:
            Catalogue.add_product(product)
            
    def test_admins_integrity(self):
        """This function test that the costumer was saved on the dictionary"""
        for user_email,admin in admins.items():
            print(f"Usermail: {user_email}, Password: {admin.password}, username: {admin.user_name}, phone: {admin.phone}, Acces: {admin.access}.")
