"""This file is a module"""
import uvicorn
from typing import List, Optional
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from users_basemodel import Admin, Customer, UserCredentials
from db_connection import session, admins, customers, products, fashion, SportFit
from product_basemodel import Product, Fashion, SportsFitness, HomeKitchen, CameraPhoto, Phone, Headphone, ConsoleAccesorie, Videogame, Laptop
from sqlalchemy.exc import IntegrityError, NoResultFound

app = FastAPI()

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

@app.post("/add-product")
async def add_product(department: str, type: Optional[str], prod: Optional[Fashion]=None):
    if department == "Fashion" and type is None:
        if prod is None:
            raise HTTPException(status_code=400, detail="Fashion product data is required")
        return await add_fashion_product(prod)
    elif department == "Sport-&-Fitness" and type is None:
        if not isinstance(prod, SportsFitness):
            raise HTTPException(status_code=400, detail="SportsFitness product data is required")
        return await add_sportfit_product(prod)
    
    raise HTTPException(status_code=400, detail="Invalid department or type")


@app.post("/add-product/Fashion")
async def add_fashion_product(prod: Fashion):
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
        raise HTTPException(status_code=500, detail="Error inserting data")

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


