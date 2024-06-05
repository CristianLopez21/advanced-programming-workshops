"This file is used to test all the normal classes using the csl"

from .n_class import users
from .n_class import product

#---------------- add product menu messages -------------------
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
#----------------------------------------------------------

custm_emailtest = input("Email: ")

def testcreatecustm(user_emailtest):
    """This function is a test"""
    user_email = user_emailtest
    password = input("Password: ")
    user_name = input("User name: ")
    phone = input("Phone number: ")
    access = False
    users.User.create_customer(user_email,password,user_name,phone,access)

costumertest = users.users[custm_emailtest]
print(type(costumertest))

admin_emailtest = input("Email: ")

def testcreateadmin():
    """This function is a test"""
    access = True
    user_email = input("Email: ")
    password = input("Password: ")
    user_name = input("User name: ")
    phone = input("Phone number: ")
    users.User.create_admin(user_email,password,user_name,phone,access)

admintest = users.users[admin_emailtest]
print(type(admintest))

def testaddpaym():
    """This function is a test for"""
    user_email = input("User name: ")
    number = input("Enter the number of the credit card")
    due_date = input("Enter the due date that appear in the credit card")
    cvv = input("Enter the cvv code that appear in the credit card")
    name = input("Enter the name that appear in the credit card")
    users.Customer.add_pay_method(costumertest, user_email, number, due_date, cvv, name)

def test_costumers_integrity():
    """This function test that the costumer was saved on the dictionary"""
    for user_email,customer in users.users.items():
        print(f"Usermail: {user_email}, Password: {customer.password}, username: {customer.user_name}, phone: {customer.phone}, Acces: {customer.access}.")
        return user_email

def test_addproduct():
    """This function is a test"""
    print(MENU_MESSAGE)
    department = int(input(" "))
    id_ = input("Enter the id for the product\n")
    name = input("Enter a name for the product: \n")
    price = input("Enter a price for the product\n")
    stock = input("Enter a stock available\n")
    description = input("Enter some info about the product\n")
    color = input("Enter the color of the product\n")
    style = input("Enter a stile option for the product\n")
    miniature = input("UPload the images of the product\n")
    print("also you can add: \n")

    if department == 1:
        fabric_type = input("Enter details about the fabrication of this product")
        care_instruction = input("Enter some care instructions ")         
        origin_country = input("Enter the origin country")
        size = input("Enter the size")
        neck_style = input("Enter information about neck style")
        sole_material = input("Enter information about sole material")
        outer_material = input("Enter some info about outer material")
        product.Product.addfashion(id_, name, price, stock, department, description, color, miniature, style, fabric_type, care_instruction, origin_country, size, neck_style, sole_material, outer_material)

    elif department == 2:
        sp_size = input("Enter the size")
        weight = input("Enter the weight of the product")
        materials = input("Enter info about materials")
        dimensions = input("Enter info about the dimensions of the product")
        use = input("Enter info ")
        age = input("Enter information such as the recommended age range for using the product.")
        product.Product.addsportfitness(id_, name, price, stock, department, description, color, miniature, style, sp_size, weight, materials, dimensions, use, age)

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
        product.Product.addhomekitchen(id_, name, price, stock, department, description, color, miniature, style, hk_size, brand, p_dimensions, shape, units, capacity, s_feature, uses, material)

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
            product.Product.addcamera(id_, name, price, stock, department, description, color, miniature, style, type_, e_brand, model, operating_system, connectivity, image, sensor_size, stabilization, shutter_s )

        elif type_ == 2:
            wireless_c = input("Enter info about the wireless carrier")
            memory = input("Enter info about the storage size")
            screen = input("Enter info about the screen size")
            battery = input("Enter info about the capacity of the battery")
            product.Product.addphone(id_, name, price, stock, department, description, color, miniature, style, type_, e_brand, model, operating_system, connectivity, wireless_c, memory, screen, battery)

        elif type_ == 3:
            form = input("Enetr the type of the headphones, example: In-Ear")
            noise = input("Enter information about noise cancellation")
            product.Product.addheadphone(id_, name, price, stock, department, description, color, miniature, style, type_, e_brand, model, operating_system, connectivity, form, noise)

        elif type_ == 4:
            platform = input("Enter info about the platform of the console")
            edition = input("Enter info about the edition of the product")
            include = input("Enter info about whta includes this product")
            devices = input("Enter info about i dont remember")
            c_memory = input("Enter the capacity of the memory")
            product.Product.addconsole(id_, name, price, stock, department, description, color, miniature, style, type_, e_brand, model, operating_system, connectivity, platform, edition, include, devices, c_memory)

        elif type_ == 5:
            v_platform = input("Enetr info about the platform of the console")
            v_edition = input("Enter info about the edition of the product")
            clasification = input("ENter info about clasification of the videogame")
            product.Product.addvideogame(id_, name, price, stock, department, description, color, miniature, style, type_, e_brand, model, operating_system, connectivity, v_platform, v_edition, clasification)

        elif type_ == 6:
            l_capacity = input("Enter info about ")
            l_screen = input("Enter the screen size of the laptop screen")
            hard_disk = input("Enter info about the hard disk of the laptop")
            cpu = input("Enter info about the laptop processor")
            ram = input("Enter info about the ram memory of the laptop")
            graphics = input("Enter info about the graphic card of the laptop")
            product.Product.addlaptop(id_, name, price, stock, department, description, color, miniature, style, type_, e_brand, model, operating_system, connectivity, l_capacity, l_screen, hard_disk, cpu, ram, graphics)

#def test_costumers_integrity(self):
#"""function test that the costumer was saved on the dictionary"""
#    for user_email,customer in costumers.items():
#        print(f"Usermail: {user_email}, Password: {customer.password}, username: {customer.user_name}, phone: {customer.phone}, Acces: {customer.access}.")
#        return user_email
