""" To do: docstring"""
from pydantic import BaseModel
from .catalogue_basemodel import Catalogue
from .product_basemodel import Product, Fashion, SportsFitness, HomeKitchen, CameraPhoto, Phone, Headphone, ConsoleAccesorie, Videogame, Laptop
from .credit_card_bm import CreditCard

#Dictionaries
costumers = {}
admins = {}
paymethods = {}
products = {}

MENU_MESSAGE = """
            Select the department to which the product belongs:
            1. Fashion
            2. Sports & fitness
            3. Home & Kitchen
            4. Electronic and accessories
        """
ELECTRONIC_MESSAGE = """
            Select the type to which the electronic belongs:
            1. Photographie and accesories
            2. Phone and accessories
            3. Headphones
            4. Console and accessories
            5. Videogames
            6. Laptops and accessories
        """


class User(BaseModel):
    """This class represents a basemodel of the user that can be use the platform"""
    user_name: str
    phone: str
    user_email: str
    password: str
    access: str

    @staticmethod
    def login(user_email: str, password: str):
        """This methood make all the process for validate the credentials of the users"""
        if user_email == user_email and  password == password:
            return User(user_name= "name",phone = "phone", user_email= user_email, password = password, access = "access")
        else:
            return False

    @staticmethod
    def create_customer():
        """This method create the object Customer and save in the database"""
        access = False
        user_email = input("Email: ")
        password = input("Password: ")
        user_name = input("User name: ")
        phone = input("Phone number: ")
        # TODO save on data base meanwhile it will be saved to a dictionary
        new_costumer = Customer(user_name,phone, user_email,password,access)
        costumers[user_email] = new_costumer

    @staticmethod
    def create_admin():
        """This method create the object Admin and save in the database"""
        access = True
        user_email = input("Email: ")
        password = input("Password: ")
        user_name = input("User name: ")
        phone = input("Phone number: ")
        # TODO save on data base meanwhile it will be saved to a dictionary
        new_admin = Admin(user_name,phone,user_email,password,access)
        admins[user_email] = new_admin

# -------------------Custumer---------------------------
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
        super().__init__(user_name= user_name, phone=phone, user_email= user_email, password=password, access= access)
        self.shipping_address = {}
        self.shoping_history = []

    def add_shipping_address(self, user_email: str):
        """This method is used to add a shipping adress for the user
        Parameters:

        - user_email
        """
        self.shipping_address[user_email] = input("Enter your shipping addres")
        #TODO save on a data base

    def add_pay_method(self, user_email: str):
        """This method is used to add a pay method for the user"""
        number = input("Enter the number of the credit card")
        due_date = input("Enter the due date that appear in the credit card")
        cvv = input("Enter the cvv code that appear in the credit card")
        name = input("Enter the name that appear in the credit card")
        new_creditcard = CreditCard(user_email, number, due_date, cvv, name)
        paymethods[user_email] = new_creditcard
        #This prints were used to validate that the data have the correct type
        # and data that was entered
        print(type(new_creditcard))
        print(f"UserMail: {user_email}, NUMBER: {number}, DUE_DATE: {due_date}, CVV: {cvv}, NAME: {name}")

    def show_history(self):
        """This method is used to show the history of the user in the platfform"""

    def test_costumers_integrity(self):
        """This function test that the costumer was saved on the dictionary"""
        for user_email,customer in costumers.items():
            print(f"Usermail: {user_email}, Password: {customer.password}, username: {customer.user_name}, phone: {customer.phone}, Acces: {customer.access}.")
            return user_email

#----------------------------Administrador_____________
class Admin(User):
    """This class represents the users that can add new products to the platform"""
    def __init__(self, user_name: str, phone: str, user_email: str, password:
                 str, access: bool):
        super().__init__(user_name=user_name, phone=phone, user_email=user_email, password=password, access=access)

    def add_product(self, access):
        """This method validate that the user have the permission, 
        if they have permission, can add products"""
        if access == True:
            print(MENU_MESSAGE)
            department = int(input(" "))
            id_ = input("Enetr the id for the product\n")
            name = input("Enter a name for the product: \n")
            stock = input("Enter a stock available\n")
            description = input("Enter some info about the product\n")
            color = input("Enter the color of the product\n")
            style = input("Enter a stile option for the product\n")
            miniature = input("UPload the images of the product\n")
            price = input("Enter a price for the product\n")
            print("also you can add: \n")
            if department == 1:
                fabric_type = input("Enter details about the fabrication of this product")
                care_instruction = input("Enter some care instructions ")         
                origin_country = input("Enter the origin country")
                size = input("Enter the size")
                neck_style = input("Enter information about neck style")
                sole_material = input("Enter information about sole material")
                outer_material = input("Enter some info about outer material")
                new_garment = Fashion(id_, name, price, stock, department, description, color, miniature, style, fabric_type, care_instruction, origin_country, size, neck_style, sole_material, outer_material)
                products[department] = new_garment
            elif department == 2:
                sp_size = input("Enter the size")
                weight = input("Enter the weight of the product")
                materials = input("Enter info about materials")
                dimensions = input("Enter info about the dimensions of the product")
                use = input("Enter info ")
                age = input("Enter information such as the recommended age range for using the product.")
                new_sport = SportsFitness(id_, name, price, stock, department, description, color, miniature, style, sp_size, weight, materials, dimensions, use, age)
                products[department] = new_sport
            elif department == 3:
                hk_size = input("Enter the size")
                brand = input("Enter the brand of the product")
                p_dimensions = input("Enter info about the dimensions of the product")
                shape = input("Enter info about the shape of the product")
                units = input("Enter some info about product units")
                capacity = input("Enter info about the capacity of the product")
                s_feature = input("if your product have a special feature you can enter here")
                uses = input("Enter info about the recommende use of the product")
                material = input("Enter info about the material of the product")
                new_homek = HomeKitchen(id_, name, price, stock, department, description, color, miniature, style, hk_size, brand, p_dimensions, shape, units, capacity, s_feature, uses, material)
                products[department] = new_homek
            elif department == 4:
                print(f"{ELECTRONIC_MESSAGE}\n")
                type_ = int(input("Enter the type of the electronic: "))
                e_brand = input("Enter the brand of the product: ")
                model = input("Enter tne model of the product: ")
                operating_system = input("Enter the version of the operating system ")
                connectivity = input("Enter the technology that the product use for conecctivity")
                if type_ == 1:
                    image = input("Enter info about the camera resolution")
                    sensor_size = input("Enter info about the size of the camera sensor")
                    stabilization = input("Enter the technology of the image stabilization")
                    shutter_s = input("Enter info about the shutter speed of the camera")
                    new_cam = CameraPhoto(id_, name, price, stock, department, description, color, miniature, style, type_, e_brand, model, operating_system, connectivity, image, sensor_size, stabilization, shutter_s )
                    products[department,type_] = new_cam
                elif type_ == 2:
                    wireless_c = input("Enter info about the wireless carrier")
                    memory = input("Enter info about the storage size")
                    screen = input("Enter info about the screen size")
                    battery = input("Enter info about the capacity of the battery")
                    new_pho = Phone(id_, name, price, stock, department, description, color, miniature, style, type_, brand, model, operating_system, connectivity, wireless_c, memory, screen, battery)
                    products[department,type_] = new_pho
                elif type_ == 3:
                    form = input("Enetr the type of the headphones, example: In-Ear")
                    noise = input("Enter information about noise cancellation")
                    new_head = Headphone(id_, name, price, stock, department, description, color, miniature, style, type_, brand, model, operating_system, connectivity, form, noise)
                    products[department,type_] = new_head
                elif type_ == 4:
                    platform = input("Enter info about the platform of the console")
                    edition = input("Enter info about the edition of the product")
                    include = input("Enter info about whta includes this product")
                    devices = input("Enter info about i dont remember")
                    c_memory = input("Enter the capacity of the memory")
                    new_cons = ConsoleAccesorie(id_, name, price, stock, department, description, color, miniature, style, type_, brand, model, operating_system, connectivity, platform, edition, include, devices, c_memory)
                    products[department, type_] = new_cons
                elif type_ == 5:
                    v_platform = input("Enetr info about the platform of the console")
                    v_edition = input("Enter info about the edition of the product")
                    clasification = input("ENter info about clasification of the videogame")
                    new_vid = Videogame(id_, name, price, stock, department, description, color, miniature, style, type_, brand, model, operating_system, connectivity, v_platform, v_edition, clasification)
                    products[department, type_] = new_vid
                elif type_ == 6:
                    l_capacity = input("Enter info about ")
                    l_screen = input("Enter the screen size of the laptop screen")
                    hard_disk = input("Enter info about the hard disk of the laptop")
                    cpu = input("Enter info about the laptop processor")
                    ram = input("Enter info about the ram memory of the laptop")
                    graphics = input("Enter info about the graphic card of the laptop")
                    new_lap = Laptop(id_, name, price, stock, department, description, color, miniature, style, type_, brand, model, operating_system, connectivity, l_capacity, l_screen, hard_disk, cpu, ram, graphics)
                    products[department, type_] = new_lap

    def test_admins_integrity(self):
        """This function test that the costumer was saved on the dictionary"""
        for user_email,admin in admins.items():
            print(f"Usermail: {user_email}, Password: {admin.password}, username: {admin.user_name}, phone: {admin.phone}, Acces: {admin.access}.")

class UserCredentials(BaseModel):
    """This class represents idk this was doing by Carlos"""
    user_email: str
    password: str
