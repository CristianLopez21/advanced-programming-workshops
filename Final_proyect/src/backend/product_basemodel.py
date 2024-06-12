"""Thsi file contains a class thar represents the behavior """
from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    """This class represent a basemodel of a Product
    
        Attributes:
        - id_ (int, optional): The unique identifier of the product.
        - name (str): The name of the product.
        - price (float): The price of the product.
        - stock (int): The stock quantity of the product.
        - department (str): The department or category the product belongs to.
        - description (str): A description of the product.
        - color (str): The color of the product.
        - style (str): The style or design of the product.
        - store (str): The store that sells the product.
    """

    id_: int = None
    name: str
    price: float
    stock: int
    department: str
    description: str
    color: str
    style: str
    store: str

#----------------------Fashion Department------------------
class Fashion(Product):
    """This class represents a base model for a product in the fashion category.

       Inherits from: 
       - Product: The product base class with common attributes such as id, name, price, stock, store, and others.

       Attributes:
       - fabric_type (str, optional): The type of fabric used for the product.
       - care (str, optional): The care instructions for the  product.
       - origin_country (str): The country of origin for the product.
       - size (str): The size of the product.
       - neck_style (str, optional): The style of the neck for the product.
       - sole_material (str, optional): The material used for the sole of the product (applicable for footwear).
       - outer_material (str, optional): The outer material used for the product. 
    """
    fabric_type: Optional[str]
    care: Optional[str]
    origin_country: str
    size: str
    neck_style: Optional[str]
    sole_material: Optional[str]
    outer_material: Optional[str]

#----------------------Sports y Fitness Department---------------------------
class SportsFitness(Product):
    """This class represents a base model for a product in the Sport-Fitness category.

       Inherits from: 
       - Product: The product base class with common attributes such as id, name, price, stock, store, and others.

       Attributes:
       - sp_size (str): The size of the product.
       - weight (str): The weight of the product.
       - materials (str): The materials used in the construction of the product.
       - item_dimensions (str): The dimensions of the product.
       - use_for (str): The intended use of the product.
       - age_range (str): The suitable age range for the product.
    """
    sp_size: str
    weight: str
    materials: str
    item_dimensions: str
    use_for: str
    age_range: str

#------------------------Home & Kitchen Department---------------------------
class HomeKitchen(Product):
    """This class represents a base model for a product in the Home-Kitchen category.

       Inherits from: 
       - Product: The product base class with common attributes such as id, name, price, stock, store, and others.

       Attributes:
       - hk_size (str): The size of product.
       - brand (str): The brand of the product.
       - product_dimensions (str): The dimensions of the product.
       - shape (str): The shape of the product.
       - units (str): The units in which the product is sold.
       - capacity (str): The capacity of product.
       - special_feature (str): Any special features of the product.
       - recommended_uses (str): Recommended uses for the product.
       - material (str): The material used in the construction of the product.
    """
    hk_size: str
    brand: str
    product_dimensions: str
    shape: str
    units: str
    capacity: str
    special_feature: str
    recommended_uses: str
    material: str

#--------------------------Electronics Department------------
class Electronic(Product):
    """This class represents a base model for a product in the Electronics category.

       Inherits from: 
       - Product: The product base class with common attributes such as id, name, price, stock, store, and others.

       Attributes:
       - type_ (str): The type of electronic product.
       - brand (str): The brand of the electronic product.
       - model_name (str): The model name of the electronic product.
       - operating_system (str): The operating system used in the electronic product.
       - connectivity_technology (str): The connectivity technology used in the electronic product."""
    type_: str
    brand: str
    model_name: str
    operating_system: str
    connectivity_technology: str

#---------------------------Electronics Types----------------------
class CameraPhoto(Electronic):
    """This class represents a base model for a product in the Electronics department,
       which in turn belongs to the CameraPhoto subdepartment.

       Inherits from: 
       - Electronic: The electronic base class with attributes inherited from the User class
         such as id, name, price, stock, and store, among others, also provides its attributes
         such as connectivity, brand, model_name, among others.

       Attributes:
       - image_resolution (str): The resolution of the camera's images.
       - photo_sensor_size (str): The size of the photo sensor in the camera.
       - image_stabilization (str): The type of image stabilization technology used in the camera.
       - shutter_speed (str): The shutter speed of the camera.
    """
    image_resolution: str
    photo_sensor_size: str
    image_stabilization: str
    shutter_speed: str

class Phone(Electronic):
    """This class represents a base model for a product in the Electronics department,
       which in turn belongs to the Phone subdepartment.

       Inherits from: 
       - Electronic: The electronic base class with attributes inherited from the User class
         such as id, name, price, stock, and store, among others, also provides its attributes
         such as connectivity, brand, model_name, among others.

       Attributes:
       - wireless_carrier (str): The wireless carrier associated with the phone.
       - memory_storage (str): The storage capacity of the phone's memory.
       - screen_size (str): The size of the phone's screen.
       - battery_power_rating (str): The power rating of the phone's battery."""
    wireless_carrier: str
    memory_storage: str
    screen_size: str
    battery_power_rating: str

class Headphone(Electronic):
    """This class represents a base model for a product in the Electronics department,
       which in turn belongs to the Headphone subdepartment.

       Inherits from: 
       - Electronic: The electronic base class with attributes inherited from the User class
         such as id, name, price, stock, and store, among others, also provides its attributes
         such as connectivity, brand, model_name, among others.

       Attributes:
       - form_factor (str): The form factor or design style of the headphones.
       - noise_cancellation (str): The type of noise cancellation technology used in the headphones."""
    form_factor: str
    noise_cancellation: str

class ConsoleAccesorie(Electronic):
    """This class represents a base model for a product in the Electronics department,
       which in turn belongs to the Console subdepartment.

       Inherits from: 
       - Electronic: The electronic base class with attributes inherited from the User class
         such as id, name, price, stock, and store, among others, also provides its attributes
         such as connectivity, brand, model_name, among others.

       Attributes:
       - platform (str): The gaming platform the accessory is designed for.
       - edition (str): The edition or version of the accessory.
       - include_components (str): The components included in the accessory package.
       - compatible_devices (str): The devices compatible with the accessory.
       - memory_storage (str): The storage capacity of the accessory, if applicable."""
    platform: str
    edition: str
    include_components: str
    compatible_devices: str
    memory_storage: str

class Videogame(Electronic):
    """This class represents the videogame category of electronics"""
    platform: str
    edition: str
    clasification: str

class Laptop(Electronic):
    """This class  represents the laptop category of electronics"""
    capacity: str
    screen_size: str
    hard_disk_size: str
    cpu: str
    ram_memory: str
    graphics_card: str
