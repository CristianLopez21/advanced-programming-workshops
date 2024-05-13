from fastapi import FastAPI
from catalogue_basemodel import Catalogue
from product_basemodel import Product
from users_basemodel import User
from users_basemodel import Customer
from users_basemodel import Admin
from credit_card import CreditCard
from typing import List
from UserCredentials import UserCredentials

app = FastAPI()

# Users


@app.post("/login", response_model=User)
def login(user_email: str, password: str):
    #TODO Add to db
    return User


@app.post("/create_customer")
def create_customer(customer: Customer) -> bool:
    # TODO Add to db
    """ """


@app.post("/create_admin")
def create_admin(admin: Admin) -> bool:
    # TODO Add to db

    """ """


# Customer


@app.post("/add_pay_method", response_model=CreditCard)
def add_pay_method():

    return CreditCard


@app.get("/show_history_get")
def show_history_get(user_email):

    return Customer.show_history(user_email)

# Admin
@app.post("admin/add_product")
def add_product(product: Product):
    Catalogue.add_product(product=Product)
