"""This file is a module"""

import uvicorn
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from users_basemodel import Admin, Customer
from db_connection import admins, session, customers

app = FastAPI()

origins = ["http://localhost", "http://localhost:8000"]
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.post("/testdatabase")
def create_admin(admin: Admin):
    """This method do some things """
    print(admin)
    query = admins.insert().values(userName= admin.user_name, phone= admin.phone,
            userEmail= admin.user_email, password= admin.password)
    session.execute(query)
    session.commit()
    return {"message":"Product created succesfully"}

def create_customer(custom: Customer):
    """This method do some things"""
    print(custom)
    query = customers.insert().values(userName= custom.user_name, phone= custom.phone,
                                      userEmail = custom.user_email, password = custom.password)
    session.execute(query)
    session.commit()
    return {"message":"User was added to the database"}

def add_shipping_addres(address, user_name):
    """This method """
    print(address)
    query = customers.update().where(customers.c.userName == user_name).values(addresdb = address)
    session.execute(query)
    session.commit()

if __name__ == "__main__":

    admin = Admin(user_name="Admin2", phone="3017808273",
                  user_email="admin2@example.com", password="4321")
    print(f"Cretae admin: {create_admin(admin)}")

    custom = Customer(user_name="Customer 1", phone="2296474",user_email="Customer1@gmail.com",password="123456")
    print(f"Create customer: {create_customer(custom)}")

    addrest = "Carrera 35 # 67-25"
    username = custom.user_name
    print(f"Update addres: {add_shipping_addres(addrest, username)}")

    uvicorn.run(app, host="0.0.0.0", port=8000)
