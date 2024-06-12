"""This file is a module"""
import uvicorn
from typing import List, Optional
from fastapi import FastAPI, HTTPException, Depends
from fastapi.middleware.cors import CORSMiddleware
from users_basemodel import Admin, Customer, UserCredentials
from db_connection import session, admins, customers, products, fashion, SportFit, homekitchen, Camera, phone, headphone, console, videogame, laptop
from product_basemodel import Product, Fashion, SportsFitness, HomeKitchen, CameraPhoto, Phone, Headphone, ConsoleAccesorie, Videogame, Laptop
from sqlalchemy.exc import IntegrityError, NoResultFound
from sqlalchemy import select

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
    print(custom)
    query = customers.insert().values(userName= custom.user_name, phone= custom.phone,
                                    userEmail = custom.user_email, password = custom.password)
    session.execute(query)
    session.commit()
    return {"message":"User was added to the database"}

@app.post("/Login")
def login(data: UserCredentials):
    try:
        # Buscar en la tabla admins
        query_admins = admins.select().where(admins.c.userEmail == data.user_email, admins.c.password == data.password)
        result_admins = session.execute(query_admins).fetchone()

        if result_admins:
            return {"message": "Admin login successful"}

        # Buscar en la tabla customers
        query_customers = customers.select().where(customers.c.userEmail == data.user_email, customers.c.password == data.password)
        result_customers = session.execute(query_customers).fetchone()

        if result_customers:
            return {"message": "Customer login successful"}

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

@app.post("/add-product/Home-&-Kitchen")
def add_homekitchen_product(prod: HomeKitchen):
    print(f"parameter: {prod} \n")
    try: 
        query = products.insert().values(name= prod.name, price= prod.price, stock= prod.stock, department= prod.department,
                                        description= prod.description, color= prod.color, style= prod.style, store= prod.store)
        result = session.execute(query)
        session.commit()
        product_id = result.inserted_primary_key[0]
        query2 = homekitchen.insert().values(proid= product_id, proname= prod.name, department= prod.department, size= prod.hk_size,
                                           brand= prod.brand, dimensions= prod.product_dimensions, shape= prod.shape, units= prod.units, capacity= prod.capacity,
                                           specialFeature= prod.special_feature, uses= prod.recommended_uses, material= prod.material)
        session.execute(query2)
        session.commit()
        return {"message": f"product {prod.name} del departamento {prod.department} se agrego con exito \n"}
    except IntegrityError as e:
        print(f"Error inserting data: {e}")
        session.rollback()

@app.post("/add-product/Electronic/Camera-Photo")
def add_cameraphoto_product(prod: CameraPhoto):
    print(f"parameter: {prod} \n")
    try: 
        query = products.insert().values(name= prod.name, price= prod.price, stock= prod.stock, department= prod.department,
                                        description= prod.description, color= prod.color, style= prod.style, store= prod.store)
        result = session.execute(query)
        session.commit()
        product_id = result.inserted_primary_key[0]
        query2 = Camera.insert().values(proid= product_id, proname= prod.name, department= prod.department, type= prod.type_, brand= prod.brand,
                                          modelname= prod.model_name, operatinSystem= prod.operating_system, connectivity= prod.connectivity_technology,
                                          imageResolution= prod.image_resolution, photoSensor= prod.photo_sensor_size, 
                                          imagestabilization= prod.image_stabilization, shutterspeed= prod.shutter_speed)
        session.execute(query2)
        session.commit()
        return {"message": f"product {prod.name} del departamento {prod.department} se agrego con exito \n"}
    except IntegrityError as e:
        print(f"Error inserting data: {e}")
        session.rollback()

@app.post("/add-product/Electronic/Phone")
def add_phone_product(prod: Phone):
    print(f"parameter: {prod} \n")
    try: 
        query = products.insert().values(name= prod.name, price= prod.price, stock= prod.stock, department= prod.department,
                                        description= prod.description, color= prod.color, style= prod.style, store= prod.store)
        result = session.execute(query)
        session.commit()
        product_id = result.inserted_primary_key[0]
        query2 = phone.insert().values(proid= product_id, proname= prod.name, department= prod.department, type= prod.type_, brand= prod.brand,
                                          modelname= prod.model_name, operatinSystem= prod.operating_system, connectivity= prod.connectivity_technology,
                                          wirelesscarrier= prod.wireless_carrier, memorystorage= prod.memory_storage, screensize= prod.screen_size, batteryrating= prod.battery_power_rating)
        session.execute(query2)
        session.commit()
        return {"message": f"product {prod.name} del departamento {prod.department} se agrego con exito \n"}
    except IntegrityError as e:
        print(f"Error inserting data: {e}")
        session.rollback()

@app.post("/add-product/Electronic/Headphone")
def add_headphone_product(prod: Headphone):
    print(f"parameter: {prod} \n")
    try: 
        query = products.insert().values(name= prod.name, price= prod.price, stock= prod.stock, department= prod.department,
                                        description= prod.description, color= prod.color, style= prod.style, store= prod.store)
        result = session.execute(query)
        session.commit()
        product_id = result.inserted_primary_key[0]
        query2 = headphone.insert().values(proid= product_id, proname= prod.name, department= prod.department, type= prod.type_, brand= prod.brand,
                                          modelname= prod.model_name, operatinSystem= prod.operating_system, connectivity= prod.connectivity_technology,
                                          formfactor= prod.form_factor, noisecancellation= prod.noise_cancellation)
        session.execute(query2)
        session.commit()
        return {"message": f"product {prod.name} del departamento {prod.department} se agrego con exito \n"}
    except IntegrityError as e:
        print(f"Error inserting data: {e}")
        session.rollback()

@app.post("/add-product/Electronic/Console-Accesories")
def add_console_accesori_product(prod: ConsoleAccesorie):
    print(f"parameter: {prod} \n")
    try: 
        query = products.insert().values(name= prod.name, price= prod.price, stock= prod.stock, department= prod.department,
                                        description= prod.description, color= prod.color, style= prod.style, store= prod.store)
        result = session.execute(query)
        session.commit()
        product_id = result.inserted_primary_key[0]
        query2 = console.insert().values(proid= product_id, proname= prod.name, department= prod.department, type= prod.type_, brand= prod.brand,
                                          modelname= prod.model_name, operatinSystem= prod.operating_system, connectivity= prod.connectivity_technology,
                                          platform= prod.platform, includecomponents= prod.include_components, compatibledevices= prod.compatible_devices,
                                          memorystorage= prod.memory_storage)
        session.execute(query2)
        session.commit()
        return {"message": f"product {prod.name} del departamento {prod.department} se agrego con exito \n"}
    except IntegrityError as e:
        print(f"Error inserting data: {e}")
        session.rollback()

@app.post("/add-product/Electronic/Videogame")
def add_videogame_product(prod: Videogame):
    print(f"parameter: {prod} \n")
    try: 
        query = products.insert().values(name= prod.name, price= prod.price, stock= prod.stock, department= prod.department,
                                        description= prod.description, color= prod.color, style= prod.style, store= prod.store)
        result = session.execute(query)
        session.commit()
        product_id = result.inserted_primary_key[0]
        query2 = videogame.insert().values(proid= product_id, proname= prod.name, department= prod.department, type= prod.type_, brand= prod.brand,
                                          modelname= prod.model_name, operatinSystem= prod.operating_system, connectivity= prod.connectivity_technology,
                                          platform= prod.platform, edition= prod.edition, clasification= prod.clasification)
        session.execute(query2)
        session.commit()
        return {"message": f"product {prod.name} del departamento {prod.department} se agrego con exito \n"}
    except IntegrityError as e:
        print(f"Error inserting data: {e}")
        session.rollback()

@app.post("/add-product/Electronic/Laptop")
def add_laptop_product(prod: Laptop):
    print(f"parameter: {prod} \n")
    try: 
        query = products.insert().values(name= prod.name, price= prod.price, stock= prod.stock, department= prod.department,
                                        description= prod.description, color= prod.color, style= prod.style, store= prod.store)
        result = session.execute(query)
        session.commit()
        product_id = result.inserted_primary_key[0]
        query2 = laptop.insert().values(proid= product_id, proname= prod.name, department= prod.department, type= prod.type_, brand= prod.brand,
                                          modelname= prod.model_name, operatinSystem= prod.operating_system, connectivity= prod.connectivity_technology,
                                         capacity= prod.capacity, screensize= prod.screen_size, harddisksize= prod.hard_disk_size, cpu= prod.cpu,
                                         ramMemory= prod.ram_memory, graphicCard= prod.graphics_card)
        session.execute(query2)
        session.commit()
        return {"message": f"product {prod.name} del departamento {prod.department} se agrego con exito \n"}
    except IntegrityError as e:
        print(f"Error inserting data: {e}")
        session.rollback()

@app.get("/catalogue/products")
def show_products() -> List[Product]:
    """This service returns all the products stored
    in the database"""

    query = products.select()
    result = session.execute(query)
    products1 = result.fetchall()

    return products1
    
@app.post("/Buy-product")
def buy_product():
    