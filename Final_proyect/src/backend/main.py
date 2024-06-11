"""This file is a module"""
import uvicorn
from typing import List
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from users_basemodel import Admin, Customer, UserCredentials
from db_connection import session, admins, customers, products, fashion, SportFit
from product_basemodel import Product, Fashion, SportsFitness, HomeKitchen, CameraPhoto, Phone, Headphone, ConsoleAccesorie, Videogame, Laptop
from sqlalchemy.exc import IntegrityError, NoResultFound

app = FastAPI()

origins = ["http://localhost", "http://localhost:8000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins= ["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/register/admin")
def create_admin(admin: Admin):
    """This method do some things """
    try:
        print(f"parameter: {admin} \n")
        query = admins.insert().values(userName= admin.user_name, phone= admin.phone,
                userEmail= admin.user_email, password= admin.password)
        session.execute(query)
        session.commit()
        return {"message":"Product created succesfully \n"}
    
    except IntegrityError as e:
        print(f"Error inserting data: {e}")
        session.rollback()
    
@app.post("/register/user")
def create_customer(custom: Customer):
    """This method do some things"""
    try:
        print(f"parameetr: {custom} \n")
        query = customers.insert().values(userName= custom.user_name, phone= custom.phone,
                                        userEmail = custom.user_email, password = custom.password)
        session.execute(query)
        session.commit()
        return {"message":"User was added to the database \n"}
    
    except IntegrityError as e:
        print(f"Error inserting data: {e}")
        session.rollback()

@app.post("/Login")
def login(data: UserCredentials):
    try:
        # Buscar en la tabla admins
        query_admins = admins.select().where(admins.c.userEmail == data.user_email, admins.c.password == data.password)
        result_admins = session.execute(query_admins).fetchone()

        if result_admins:
            return {"message": "Admin login successful", "user": result_admins}

        # Buscar en la tabla customers
        query_customers = customers.select().where(customers.c.userEmail == data.user_email, customers.c.password == data.password)
        result_customers = session.execute(query_customers).fetchone()

        if result_customers:
            return {"message": "Customer login successful", "user": result_customers}

        # Si no se encontró en ninguna tabla
        return {"message": "Incorrect username or password"}

    except NoResultFound:
        return {"message": "Incorrect username or password"}

@app.put("/user/addres")
def add_shipping_addres(address, user_name):
    """This method """
    try:
        print(f"parameter: {address} \n")
        query = customers.update().where(customers.c.userName == user_name).values(addresdb = address)
        session.execute(query)
        session.commit()
        return {"message": "address added successfully \n"}
    
    except IntegrityError as e:
        print(f"Error inserting data: {e}")
        session.rollback()

@app.post("/add-product/Fashion")
def add_fashion_product(prod: Fashion):
    print(f"parameter: {prod} \n")
    try: 
        query = products.insert().values(name= prod.name, price= prod.price, stock= prod.stock, department= prod.department,
                                        description= prod.description, color= prod.color, style= prod.style, store= prod.store)
        result = session.execute(query)
        session.commit()
        product_id = result.inserted_primary_key[0]
        query2 = fashion.insert().values(proid= product_id, proname= prod.name, department= prod.department,
                                         fabricType= prod.fabric_type, care= prod.care, originCountry= prod.origin_country,
                                         size= prod.size, neckStyle= prod.neck_style, soleMaterial= prod.sole_material, outerMaterial= prod.outer_material)
        session.execute(query2)
        session.commit()
        return {"message": f"product {prod.name} del departamento {prod.department} se agrego con exito \n"}
    except IntegrityError as e:
        print(f"Error inserting data: {e}")
        session.rollback()

@app.post("/add-product/Sport-&-Fitness")
def add_sportfit_product(prod: SportsFitness):
    print(f"parameter: {prod} \n")
    try: 
        query = products.insert().values(name= prod.name, price= prod.price, stock= prod.stock, department= prod.department,
                                        description= prod.description, color= prod.color, style= prod.style, store= prod.store)
        result = session.execute(query)
        session.commit()
        product_id = result.inserted_primary_key[0]
        query2 = SportFit.insert().values(proid= product_id, proname= prod.name, department= prod.department,
                                          size= prod.sp_size, weight= prod.weight, materials= prod.materials,
                                         dimensions= prod.item_dimensions, useFor= prod.use_for, ageRange= prod.age_range)
        session.execute(query2)
        session.commit()
        return {"message": f"product {prod.name} del departamento {prod.department} se agrego con exito \n"}
    except IntegrityError as e:
        print(f"Error inserting data: {e}")
        session.rollback()

def add_homekitchen_product(prod: HomeKitchen):
    pass

def add_cameraphoto_product(prod: CameraPhoto):
    pass

def add_phone_product(prod: Phone):
    pass

def add_headphone_product(prod: Headphone):
    pass

def add_console_accesori_product(prod: ConsoleAccesorie):
    pass

def add_videogame_product(prod: Videogame):
    pass

def add_laptop_product(prod: Laptop):
    pass

def show_products() -> List[Product]:
    """This service returns all the products stored
    in the database"""

    query = products.select()
    result = session.execute(query)
    products = result.fetchall()

    return products


if __name__ == "__main__":

    admin = Admin(user_name="Admin2", phone="3017808273",
                  user_email="admin2@example.com", password="4321")
    print(f"Cretae admin: {create_admin(admin)}")
    custom = Customer(user_name="Customer 1", phone="2296474",user_email="Customer1@gmail.com",password="123456")
    print(f"Create customer: {create_customer(custom)}")
    addrest = "Carrera 36 # 67-25"
    username = custom.user_name
    print(f"Update addres: {add_shipping_addres(addrest, username)}")

    fashion1 = Fashion(name="Product2", price="1250.09", stock=20, department="fashion",
                    description="description1", color="blue", style="idk", store="Bmazon",fabric_type="IDK",
                    care="not wash machine", origin_country="Colombian", size="M", neck_style="Not available",
                    sole_material="no aplica", outer_material="no aplica")
    print(f"Add fashion product: {add_fashion_product(fashion1)}")

    sport1 = SportsFitness(name="sport1", price="120.99", stock=10, department="Sport & Fitness", description="Description sport",
                           color="White", style="IDK", store="Bmazon", sp_size="XL", weight="20 kg", materials="plastic",
                            item_dimensions= "100 x 200 x 20 LxAxAL", use_for="None", age_range="7+")
    print(f"Add sport product: {add_sportfit_product(sport1)}")
