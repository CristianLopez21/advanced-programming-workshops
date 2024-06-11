"""Thsi file contains a class thar represents the behavior """
from pydantic import BaseModel
from typing import Optional

class Product(BaseModel):
    """This class represent a basemodel of a Product"""

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
    """This class represents the fashion category of products"""
    fabric_type: Optional[str]
    care: Optional[str]
    origin_country: str
    size: str
    neck_style: Optional[str]
    sole_material: Optional[str]
    outer_material: Optional[str]

#----------------------Sports y Fitness Department---------------------------
class SportsFitness(Product):
    """This class represents the soport-fitness category of products"""
    sp_size: str
    weight: str
    materials: str
    item_dimensions: str
    use_for: str
    age_range: str

#------------------------Home & Kitchen Department---------------------------
class HomeKitchen(Product):
    """This class represents the home-kitchen category of products"""
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
    """This class represents the electronics category of products"""
    type_: str
    brand: str
    model_name: str
    operating_system: str
    connectivity_technology: str

#---------------------------Electronics Types----------------------
class CameraPhoto(Electronic):
    """This class represents the camera photo category of electronicss"""
    image_resolution: str
    photo_sensor_size: str
    image_stabilization: str
    shutter_speed: str

class Phone(Electronic):
    """This class represents the phone category of electronics"""
    wireless_carrier: str
    memory_storage: str
    screen_size: str
    battery_power_rating: str

class Headphone(Electronic):
    """This class represents the headphone category of electronics"""
    form_factor: str
    noise_cancellation: str

class ConsoleAccesorie(Electronic):
    """This class  represents the console accesories category of electronics"""
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
