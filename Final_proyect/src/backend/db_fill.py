from users_basemodel import Admin, Customer
from product_basemodel import Fashion, SportsFitness, HomeKitchen, CameraPhoto, Phone, Headphone, ConsoleAccesorie, Videogame, Laptop
from main import create_admin, create_customer, add_shipping_addres, add_fashion_product, add_sportfit_product, add_homekitchen_product, add_cameraphoto_product, add_phone_product, add_headphone_product, add_console_accesory_product, add_videogame_product, add_laptop_product

admin1 = Admin(user_name="Admin1", phone="3017808273",
              user_email="admin1@example.com", password="4321")
create_admin(admin1)

admin2 = Admin(user_name="Admin2", phone="+57 3128874832",
              user_email="admin2@example.com", password="1234")
create_admin(admin2)

admin3 = Admin(user_name="Admin3", phone="31237820293",
              user_email="admin1@example.com", password="918273")
create_admin(admin3)

custom1 = Customer(user_name="Customer1", phone="2296474",user_email="Customer1@gmail.com",
                  password="123456789")
create_customer(custom1)

custom2 = Customer(user_name="Customer2", phone="3002296474",user_email="Customer2@gmail.com",
                  password="123456789")
create_customer(custom2)

custom3 = Customer(user_name="Customer3", phone="3122296474",user_email="Customer3@gmail.com",
                  password="123456789")
create_customer(custom3)

address1 = "Carrera 36 # 67-25"
username1 = custom1.user_name
add_shipping_addres(address1, username1)

address2 = "Calle 68 # 37-22b"
username2 = custom2.user_name
add_shipping_addres(address2, username2)

address3 = "Carrera 167b # 17-35"
username3 = custom3.user_name
add_shipping_addres(address3, username3)

fashion1 = Fashion(name="Product2", price="1250.09", stock=20, department="fashion",
                description="description1", color="blue", style="idk", store="Bmazon",fabric_type="IDK",
                care="not wash machine", origin_country="Colombian", size="M", neck_style="Not available",
                sole_material="no aplica", outer_material="no aplica")
print(f"Add fashion product: {add_fashion_product(fashion1)}")

fashion2 = Fashion(
    name="Product3", 
    price="799.99", 
    stock=30, 
    department="fashion", 
    description="description2", 
    color="red", 
    style="casual", 
    store="Bmazon", 
    fabric_type="cotton", 
    care="machine wash cold", 
    origin_country="Mexican", 
    size="L", 
    neck_style="V-neck", 
    sole_material="no aplica", 
    outer_material="cotton"
)
print(f"Add fashion product: {add_fashion_product(fashion2)}")

fashion3 = Fashion(
    name="Product4", 
    price="1999.99", 
    stock=10, 
    department="fashion", 
    description="description3", 
    color="black", 
    style="formal", 
    store="Bmazon", 
    fabric_type="silk", 
    care="dry clean only", 
    origin_country="Italian", 
    size="S", 
    neck_style="collar", 
    sole_material="no aplica", 
    outer_material="silk"
)
print(f"Add fashion product: {add_fashion_product(fashion3)}")

sport1 = SportsFitness(name="sport1", price="120.99", stock=10, department="Sport & Fitness", description="Description sport",
                      color="White", style="IDK", store="Bmazon", sp_size="XL", weight="20 kg", materials="plastic",
                    item_dimensions= "100 x 200 x 20 LxAxAL", use_for="None", age_range="7+")
add_sportfit_product(sport1)

sport2 = SportsFitness(
    name="sport2", 
    price="89.99", 
    stock=15, 
    department="Sport & Fitness", 
    description="Description sport2", 
    color="Black", 
    style="Sporty", 
    store="Bmazon", 
    sp_size="M", 
    weight="10 kg", 
    materials="metal", 
    item_dimensions="80 x 150 x 15 LxAxAL", 
    use_for="Outdoor", 
    age_range="10+"
)
add_sportfit_product(sport2)

sport3 = SportsFitness(
    name="sport3", 
    price="150.00", 
    stock=5, 
    department="Sport & Fitness", 
    description="Description sport3", 
    color="Blue", 
    style="Modern", 
    store="Bmazon", 
    sp_size="L", 
    weight="25 kg", 
    materials="carbon fiber", 
    item_dimensions="90 x 180 x 20 LxAxAL", 
    use_for="Indoor", 
    age_range="12+"
)
add_sportfit_product(sport3)

# Definición del objeto home1
home1 = HomeKitchen(
    name="HomeProduct1", 
    price="299.99", 
    stock=30, 
    department="Home & Kitchen", 
    description="A versatile kitchen appliance", 
    color="Silver", 
    style="Modern", 
    store="Bmazon", 
    hk_size="Large", 
    brand="KitchenAid", 
    product_dimensions="30 x 40 x 50 cm", 
    shape="Rectangular", 
    units="1 piece", 
    capacity="5 liters", 
    special_feature="Dishwasher safe", 
    recommended_uses="Cooking", 
    material="Stainless steel"
)

# Definición del objeto home2
home2 = HomeKitchen(
    name="HomeProduct2", 
    price="159.99", 
    stock=50, 
    department="Home & Kitchen", 
    description="A cozy and comfortable blanket", 
    color="Blue", 
    style="Casual", 
    store="Bmazon", 
    hk_size="Queen", 
    brand="ComfortCo", 
    product_dimensions="220 x 240 cm", 
    shape="Square", 
    units="1 piece", 
    capacity="Not applicable", 
    special_feature="Hypoallergenic", 
    recommended_uses="Sleeping", 
    material="Cotton"
)

# Definición del objeto home3
home3 = HomeKitchen(
    name="HomeProduct3", 
    price="79.99", 
    stock=100, 
    department="Home & Kitchen", 
    description="A set of premium kitchen knives", 
    color="Black", 
    style="Elegant", 
    store="Bmazon", 
    hk_size="Medium", 
    brand="Chef's Choice", 
    product_dimensions="30 x 20 x 5 cm", 
    shape="Assorted", 
    units="6 pieces", 
    capacity="Not applicable", 
    special_feature="Razor sharp blades", 
    recommended_uses="Cutting", 
    material="High-carbon stainless steel"
)

# Imprimir los resultados de agregar los productos
add_homekitchen_product(home1)
add_homekitchen_product(home2)
add_homekitchen_product(home3)

# Definición del objeto cam1
cam1 = CameraPhoto(
    name="CamProduct1", 
    price="1299.99", 
    stock=15, 
    department="Electronics", 
    description="A high-quality DSLR camera", 
    color="Black", 
    style="Professional", 
    store="Bmazon", 
    type_="CameraPhoto", 
    brand="Canon", 
    model_name="EOS 90D", 
    operating_system="None", 
    connectivity_technology="Wi-Fi", 
    image_resolution="32.5 MP", 
    photo_sensor_size="APS-C", 
    image_stabilization="Optical", 
    shutter_speed="1/8000 sec"
)

# Definición del objeto cam2
cam2 = CameraPhoto(
    name="CamProduct2", 
    price="899.99", 
    stock=25, 
    department="Electronics", 
    description="A compact mirrorless camera", 
    color="Silver", 
    style="Modern", 
    store="Bmazon", 
    type_="CameraPhoto", 
    brand="Sony", 
    model_name="Alpha a6000", 
    operating_system="None", 
    connectivity_technology="Wi-Fi, NFC", 
    image_resolution="24.3 MP", 
    photo_sensor_size="APS-C", 
    image_stabilization="None", 
    shutter_speed="1/4000 sec"
)

# Definición del objeto cam3
cam3 = CameraPhoto(
    name="CamProduct3", 
    price="499.99", 
    stock=40, 
    department="Electronics", 
    description="A versatile point-and-shoot camera", 
    color="Red", 
    style="Casual", 
    store="Bmazon", 
    type_="CameraPhoto", 
    brand="Nikon", 
    model_name="Coolpix B600", 
    operating_system="None", 
    connectivity_technology="Bluetooth, Wi-Fi", 
    image_resolution="16 MP", 
    photo_sensor_size="1/2.3 inch", 
    image_stabilization="Optical", 
    shutter_speed="1/1500 sec"
)

# Imprimir los resultados de agregar los productos
add_cameraphoto_product(cam1)
add_cameraphoto_product(cam2)
add_cameraphoto_product(cam3)

# Definición del objeto phone1
phone1 = Phone(
    name="PhoneProduct1", 
    price="999.99", 
    stock=20, 
    department="Electronics", 
    description="A high-end smartphone with excellent features", 
    color="Black", 
    style="Sleek", 
    store="Bmazon", 
    type_="Phone", 
    brand="Apple", 
    model_name="iPhone 13 Pro", 
    operating_system="iOS", 
    connectivity_technology="5G, Wi-Fi, Bluetooth", 
    wireless_carrier="Unlocked", 
    memory_storage="256 GB", 
    screen_size="6.1 inches", 
    battery_power_rating="3095 mAh"
)

# Definición del objeto phone2
phone2 = Phone(
    name="PhoneProduct2", 
    price="799.99", 
    stock=30, 
    department="Electronics", 
    description="A powerful Android phone with a great camera", 
    color="Blue", 
    style="Modern", 
    store="Bmazon", 
    type_="Phone", 
    brand="Samsung", 
    model_name="Galaxy S21", 
    operating_system="Android", 
    connectivity_technology="5G, Wi-Fi, Bluetooth", 
    wireless_carrier="Unlocked", 
    memory_storage="128 GB", 
    screen_size="6.2 inches", 
    battery_power_rating="4000 mAh"
)

# Definición del objeto phone3
phone3 = Phone(
    name="PhoneProduct3", 
    price="499.99", 
    stock=50, 
    department="Electronics", 
    description="A budget-friendly phone with all essential features", 
    color="White", 
    style="Casual", 
    store="Bmazon", 
    type_="Phone", 
    brand="Google", 
    model_name="Pixel 5a", 
    operating_system="Android", 
    connectivity_technology="5G, Wi-Fi, Bluetooth", 
    wireless_carrier="Unlocked", 
    memory_storage="128 GB", 
    screen_size="6.34 inches", 
    battery_power_rating="4680 mAh"
)

# Imprimir los resultados de agregar los productos
add_phone_product(phone1)
add_phone_product(phone2)
add_phone_product(phone3)

# Definición del objeto headphone1
headphone1 = Headphone(
    name="HeadphoneProduct1", 
    price="299.99", 
    stock=40, 
    department="Electronics", 
    description="High-fidelity wireless over-ear headphones", 
    color="Black", 
    style="Over-Ear", 
    store="Bmazon", 
    type_="Headphone", 
    brand="Bose", 
    model_name="QuietComfort 35 II", 
    operating_system="None", 
    connectivity_technology="Bluetooth, Wired", 
    form_factor="Over-Ear", 
    noise_cancellation="Active"
)

# Definición del objeto headphone2
headphone2 = Headphone(
    name="HeadphoneProduct2", 
    price="199.99", 
    stock=30, 
    department="Electronics", 
    description="Comfortable in-ear headphones with excellent sound quality", 
    color="White", 
    style="In-Ear", 
    store="Bmazon", 
    type_="Headphone", 
    brand="Sony", 
    model_name="WF-1000XM4", 
    operating_system="None", 
    connectivity_technology="Bluetooth", 
    form_factor="In-Ear", 
    noise_cancellation="Active"
)

# Definición del objeto headphone3
headphone3 = Headphone(
    name="HeadphoneProduct3", 
    price="149.99", 
    stock=50, 
    department="Electronics", 
    description="Affordable on-ear headphones with noise isolation", 
    color="Blue", 
    style="On-Ear", 
    store="Bmazon", 
    type_="Headphone", 
    brand="JBL", 
    model_name="Live 460NC", 
    operating_system="None", 
    connectivity_technology="Bluetooth, Wired", 
    form_factor="On-Ear", 
    noise_cancellation="Passive"
)

# Imprimir los resultados de agregar los productos
add_headphone_product(headphone1)
add_headphone_product(headphone2)
add_headphone_product(headphone3)

# Definición del objeto console_acc1
console_acc1 = ConsoleAccesorie(
    name="ConsoleAccessoryProduct1", 
    price="59.99", 
    stock=100, 
    department="Electronics", 
    description="Wireless controller for PlayStation 5", 
    color="White", 
    style="Modern", 
    store="Bmazon", 
    type_="ConsoleAccesorie", 
    brand="Sony", 
    model_name="DualSense", 
    operating_system="None", 
    connectivity_technology="Bluetooth", 
    platform="PlayStation 5", 
    edition="Standard", 
    include_components="Controller, USB-C cable", 
    compatible_devices="PlayStation 5", 
    memory_storage="None"
)

# Definición del objeto console_acc2
console_acc2 = ConsoleAccesorie(
    name="ConsoleAccessoryProduct2", 
    price="29.99", 
    stock=150, 
    department="Electronics", 
    description="Charging dock for Xbox Series X controllers", 
    color="Black", 
    style="Compact", 
    store="Bmazon", 
    type_="ConsoleAccesorie", 
    brand="Microsoft", 
    model_name="Xbox Dual Charging Station", 
    operating_system="None", 
    connectivity_technology="Wired", 
    platform="Xbox Series X", 
    edition="Standard", 
    include_components="Charging dock, 2 rechargeable batteries", 
    compatible_devices="Xbox Series X controllers", 
    memory_storage="None"
)

# Definición del objeto console_acc3
console_acc3 = ConsoleAccesorie(
    name="ConsoleAccessoryProduct3", 
    price="99.99", 
    stock=50, 
    department="Electronics", 
    description="VR headset for PC gaming", 
    color="Black", 
    style="Ergonomic", 
    store="Bmazon", 
    type_="ConsoleAccesorie", 
    brand="Oculus", 
    model_name="Quest 2", 
    operating_system="None", 
    connectivity_technology="Wireless", 
    platform="PC", 
    edition="128 GB", 
    include_components="VR headset, controllers, charger", 
    compatible_devices="PC", 
    memory_storage="128 GB"
)

# Imprimir los resultados de agregar los productos
add_console_accesory_product(console_acc1)
add_console_accesory_product(console_acc2)
add_console_accesory_product(console_acc3)

# Definición del objeto videogame1
videogame1 = Videogame(
    name="VideogameProduct1", 
    price="69.99", 
    stock=200, 
    department="Electronics", 
    description="A thrilling action-adventure game", 
    color="N/A", 
    style="N/A", 
    store="Bmazon", 
    type_="Videogame", 
    brand="Ubisoft", 
    model_name="Assassin's Creed Valhalla", 
    operating_system="None", 
    connectivity_technology="N/A", 
    platform="PlayStation 5", 
    edition="Standard", 
    clasification="Mature"
)

# Definición del objeto videogame2
videogame2 = Videogame(
    name="VideogameProduct2", 
    price="59.99", 
    stock=300, 
    department="Electronics", 
    description="An engaging role-playing game", 
    color="N/A", 
    style="N/A", 
    store="Bmazon", 
    type_="Videogame", 
    brand="Square Enix", 
    model_name="Final Fantasy VII Remake", 
    operating_system="None", 
    connectivity_technology="N/A", 
    platform="PlayStation 4", 
    edition="Deluxe", 
    clasification="Teen"
)

# Definición del objeto videogame3
videogame3 = Videogame(
    name="VideogameProduct3", 
    price="49.99", 
    stock=150, 
    department="Electronics", 
    description="A popular sports simulation game", 
    color="N/A", 
    style="N/A", 
    store="Bmazon", 
    type_="Videogame", 
    brand="EA Sports", 
    model_name="FIFA 22", 
    operating_system="None", 
    connectivity_technology="N/A", 
    platform="Xbox One", 
    edition="Standard", 
    clasification="Everyone"
)

# Imprimir los resultados de agregar los productos
add_videogame_product(videogame1)
add_videogame_product(videogame2)
add_videogame_product(videogame3)

# Definición del objeto laptop1
laptop1 = Laptop(
    name="LaptopProduct1", 
    price="1299.99", 
    stock=50, 
    department="Electronics", 
    description="High-performance laptop for gaming and professional use", 
    color="Black", 
    style="Modern", 
    store="Bmazon", 
    type_="Laptop", 
    brand="Dell", 
    model_name="XPS 15", 
    operating_system="Windows 11", 
    connectivity_technology="Wi-Fi, Bluetooth", 
    capacity="1 TB SSD", 
    screen_size="15.6 inches", 
    hard_disk_size="1 TB", 
    cpu="Intel Core i7", 
    ram_memory="16 GB", 
    graphics_card="NVIDIA GeForce GTX 1650"
)

# Definición del objeto laptop2
laptop2 = Laptop(
    name="LaptopProduct2", 
    price="999.99", 
    stock=30, 
    department="Electronics", 
    description="Lightweight and portable laptop for everyday use", 
    color="Silver", 
    style="Sleek", 
    store="Bmazon", 
    type_="Laptop", 
    brand="Apple", 
    model_name="MacBook Air", 
    operating_system="macOS", 
    connectivity_technology="Wi-Fi, Bluetooth", 
    capacity="512 GB SSD", 
    screen_size="13.3 inches", 
    hard_disk_size="512 GB", 
    cpu="Apple M1", 
    ram_memory="8 GB", 
    graphics_card="Apple M1"
)

# Definición del objeto laptop3
laptop3 = Laptop(
    name="LaptopProduct3", 
    price="699.99", 
    stock=70, 
    department="Electronics", 
    description="Affordable laptop for students and basic tasks", 
    color="Blue", 
    style="Casual", 
    store="Bmazon", 
    type_="Laptop", 
    brand="HP", 
    model_name="Pavilion 14", 
    operating_system="Windows 10", 
    connectivity_technology="Wi-Fi, Bluetooth", 
    capacity="256 GB SSD", 
    screen_size="14 inches", 
    hard_disk_size="256 GB", 
    cpu="AMD Ryzen 5", 
    ram_memory="8 GB", 
    graphics_card="AMD Radeon Vega 8"
)

# Imprimir los resultados de agregar los productos
add_laptop_product(laptop1)
add_laptop_product(laptop2)
add_laptop_product(laptop3)
