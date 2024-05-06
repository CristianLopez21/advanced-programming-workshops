from fastapi import FastAPI
from catalogue_basemodel import Catalogue
from product_basemodel import Product
from users_basemodel import User
from users_basemodel import Customer    
from users_basemodel import Admin
from typing import List
from UserCredentials import UserCredentials
app = FastAPI()

#Users 

@app.post("/login", response_model=User)
def login(credentials: UserCredentials):
    return User.login(credentials.user_email, credentials.password)

@app.post ("/create_customer")
def create_customer(customer: Customer):
    pass

@app.post("/create_admin")
def create_admin(admin: Admin):
    pass

#Customer
@app.post("/add_shipping_adress")
def add_shipping_adress(user_email):
    return Customer.add_shipping_address(user_email)

@app.post("/add_pay_method")
def add_pay_method(user_email):
    return Customer.add_pay_method(user_email)

@app.get("/show_history_get")
def show_history_get():
    pass   

#Admin
@app.post("admin/add_product")
def add_product(product:Product):
    Catalogue.add_product(product=Product)