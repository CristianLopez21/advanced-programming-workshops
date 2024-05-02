from pydantic import BaseModel


class Product(BaseModel):
    """This class represent a basemodel of a Product"""

    id: str
    name: str
    price: float
    stock: int
    department: str
    description: str
    color: str
    style: str

#----------------------Fashion Department------------------
class Fashion(Product):
    """This class represents the fashion category of products"""
    def __init__(self, id: str, name: str, price: float, stock: int, department: str,
                 description: str, color: str, miniature, style: str, fabric_type:str,
                 care_instruction:str, origin_country:str, size:str,
                 neck_style:str, sole_material:str, outer_material:str) :
        super().__init__(id=id, name=name, price=price, stock=stock, department= department, description=description, color=color, miniature=miniature, style=style)
        self.fabric_type = fabric_type
        self.care = care_instruction
        self.origin_country = origin_country
        self.size = size
        self.neck_style = neck_style
        self.sole_material = sole_material
        self.outer_material = outer_material

#----------------------Sports y Fitness Department---------------------------
class SportsFitness(Product):
    """This class represents the soport-fitness category of products"""
    def __init__(self, id: str, name: str, price: float, stock: int, department: str,
                 description: str, color: str, miniature, style: str, sp_size:str,
                 weight:str, materials:str, item_dimensions:str, use_for:str, age_range:str):
        super().__init__(id=id, name=name, price=price, stock=stock, department= department, description=description, color=color, miniature=miniature, style=style)
        self.sp_size = sp_size
        self.weight = weight
        self.materials = materials
        self.item_dimensions = item_dimensions
        self.use_for = use_for
        self.age_range = age_range


#------------------------Home & Kitchen Department---------------------------
class HomeKitchen(Product):
    """This class represents the home-kitchen category of products"""
    def __init__(self, id: str, name: str, price: float, stock: int, department: str,
                 description: str, color: str, miniature, style: str, hk_size:str, brand:str,
                 product_dimensions:str, shape:str, units:str, capacity:str, special_feature:str,
                 recommended_uses:str, material:str):
        super().__init__(id=id, name=name, price=price, stock=stock, department= department, description=description, color=color, miniature=miniature, style=style)
        self.hk_size = hk_size
        self.brand = brand
        self.product_dimensions = product_dimensions
        self.shape = shape
        self.units = units
        self.capacity = capacity
        self.special_feature = special_feature
        self.recommended_uses = recommended_uses
        self.material = material

#--------------------------Electronics Department------------
class Electronic(Product):
    """This class represents the electronics category of products"""
    def __init__(self, id: str, name: str, price: float, stock: int, department: str,
                 description: str, color: str, miniature, style: str, type_:str, brand:str,
                 model_name:str, operating_system:str, connectivity_technology:str):
        super().__init__(id=id, name=name, price=price, stock=stock, department= department, description=description, color=color, miniature=miniature, style=style)
        self.type_ = type_
        self.brand = brand
        self.model_name = model_name
        self.operating_system = operating_system
        self.connectivity_technology = connectivity_technology

#---------------------------Electronics Types----------------------
class CameraPhoto(Electronic):
    """This class represents the camera photo category of electronicss"""
    def __init__(self, id: str, name: str, price: float, stock: int, department: str,
                 description: str, color: str, miniature, style: str, type_: str,
                 brand: str, model_name: str, operating_system: str, connectivity_technology: str,
                 image_resolution:str, photo_sensor_size:str, image_stabilization: str, shutter_speed:str):
        super().__init__(id, name, price, stock, department, description, color, miniature, style,
                         type_, brand, model_name, operating_system, connectivity_technology)
        self.image_resolution = image_resolution
        self.photo_sensor_size = photo_sensor_size
        self.image_stabilization = image_stabilization
        self.shutter_speed = shutter_speed

class Phone(Electronic):
    """This class represents the phone category of electronics"""
    def __init__(self, id: str, name: str, price: float, stock: int, department: str, description: str,
                 color: str, miniature, style: str, type_: str, brand: str, model_name: str,
                 operating_system: str, connectivity_technology: str, wireless_carrier:str,
                 memory_storage:str, screen_size:str, battery_power_rating:str):
        super().__init__(id, name, price, stock, department, description, color, miniature, style,
                         type_, brand, model_name, operating_system, connectivity_technology)
        self.wireless_carrier = wireless_carrier
        self.memory_storage = memory_storage
        self.screen_size = screen_size
        self.battery_power_rating = battery_power_rating

class Headphone(Electronic):
    """This class represents the headphone category of electronics"""
    def __init__(self, id: str, name: str, price: float, stock: int, department: str, description: str,
                 color: str, miniature, style: str, type_: str, brand: str,
                 model_name: str, operating_system: str, connectivity_technology: str,
                    form_factor:str, noise_cancellation:str):
        super().__init__(id, name, price, stock, department, description, color, miniature, 
                         style, type_, brand, model_name, operating_system, connectivity_technology)
        self.form_factor = form_factor
        self.noise_cancellation = noise_cancellation

class ConsoleAccesorie(Electronic):
    """This class  represents the console accesories category of electronics"""
    def __init__(self, id: str, name: str, price: float, stock: int, department: str, description: str,
                 color: str, miniature, style: str, type_: str, brand: str, model_name: str,
                 operating_system: str, connectivity_technology: str, platform:str, edition:str,
                 include_components:str, compatible_devices:str, memory_storage:str):
        super().__init__(id, name, price, stock, department, description, color, miniature,
                         style, type_, brand, model_name, operating_system, connectivity_technology)
        self.platform = platform
        self.edition = edition
        self.include_components = include_components
        self.compatible_devices = compatible_devices
        self.memory_storage = memory_storage

class Videogame(Electronic):
    """This class represents the videogame category of electronics"""
    def __init__(self, id: str, name: str, price: float, stock: int, department: str, description: str,
                 color: str, miniature, style: str, type_: str, brand: str, model_name: str,
                 operating_system: str, connectivity_technology: str, platform:str, edition:str,
                 clasification:str):
        super().__init__(id, name, price, stock, department, description, color, miniature,
                         style, type_, brand, model_name, operating_system, connectivity_technology)
        self.platform = platform
        self.edition = edition
        self.clasification = clasification

class Laptop(Electronic):
    """This class  represents the laptop category of electronics"""
    def __init__(self, id: str, name: str, price: float, stock: int, department: str, description: str,
                 color: str, miniature, style: str, type_: str, brand: str, model_name: str,
                 operating_system: str, connectivity_technology: str, capacity:str,
                 screen_size:str, hard_disk_size:str, cpu:str, ram_memory:str, graphics_card:str):
        super().__init__(id, name, price, stock, department, description, color, miniature,
                         style, type_, brand, model_name, operating_system, connectivity_technology)
        self.capacity = capacity
        self.screen_size = screen_size
        self.hard_disk_size = hard_disk_size
        self.cpu = cpu
        self.ram_memory = ram_memory
        self.graphics_card = graphics_card