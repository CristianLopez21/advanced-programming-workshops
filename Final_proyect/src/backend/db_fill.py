from users_basemodel import Admin, Customer, UserCredentials
from product_basemodel import Fashion, SportsFitness
from main import show_products, create_admin, create_customer, add_shipping_addres, add_fashion_product, add_sportfit_product, login
from db_connection import session, products, fashion
from typing import List
from sqlalchemy import select


    #admin = Admin(user_name="Admin2", phone="3017808273",
    #              user_email="admin2@example.com", password="4321")
    #print(f"Cretae admin: {create_admin(admin)}")

    #custom = Customer(user_name="Customer 2", phone="2296474",user_email="Customer2@gmail.com",
    #                  password="123456789")
    #print(f"Create customer: {create_customer(custom)}")

    #credential = UserCredentials(user_email="Customer2@gmail.com", password="123456789")
    #print(f"Login: {login(credential)} --end\n")

    #addrest = "Carrera 36 # 67-25"
    #username = custom.user_name
    #print(f"Update addres: {add_shipping_addres(addrest, username)}")

    #fashion1 = Fashion(name="Product2", price="1250.09", stock=20, department="fashion",
    #                description="description1", color="blue", style="idk", store="Bmazon",fabric_type="IDK",
    #                care="not wash machine", origin_country="Colombian", size="M", neck_style="Not available",
    #                sole_material="no aplica", outer_material="no aplica")
    #print(f"Add fashion product: {add_fashion_product(fashion1)}")

    #sport1 = SportsFitness(name="sport1", price="120.99", stock=10, department="Sport & Fitness", description="Description sport",
    #                      color="White", style="IDK", store="Bmazon", sp_size="XL", weight="20 kg", materials="plastic",
    #                    item_dimensions= "100 x 200 x 20 LxAxAL", use_for="None", age_range="7+")
    #print(f"Add sport product: {add_sportfit_product(sport1)}")

    #show_products()

query = select(
    
)
result = session.execute(query)
products1 = result.fetchall()
query2 = select(
        fashion.c.fabricType,
        fashion.c.care,
        fashion.c.originCountry,
        fashion.c.size,
        fashion.c.neckStyle,
        fashion.c.soleMaterial,
        fashion.c.outerMaterial
        )
result = session.execute(query2)
products2 = result.fetchall()
print(f"prod type: {type(products1)}_ values: {products1}, \n fashion type: {type(products2)}_ values {products2}\n .....end \n")