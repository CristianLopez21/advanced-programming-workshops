from fastapi import FastAPI
from catalogue import Catalogue
from product_basemodel import Product
from users_basemodel import User
from users_basemodel import Customer
from users_basemodel import Admin
from credit_card import CreditCard
from models import UserCredentials
import uvicorn


app = FastAPI()

# Users


@app.post("/login", response_model=User)
def login(credentials: UserCredentials):
    #TODO Add to db
    return User.login(credentials.user_email, credentials.password)


@app.post("/create_customer")
def create_customer(customer: Customer)-> bool:
    # TODO Add to db
    """ """


@app.post("/create_admin")
def create_admin(admin: Admin)-> bool:
    # TODO Add to db

    """ """


# Customer




@app.get("/show_history_get")
def show_history_get(user_email):

    return Customer.show_history(user_email)

# Admin
@app.post("admin/add_product")
def add_product(product: Product):
    Catalogue.add_product(product)

if __name__ == "__main__":
    uvicorn.run(app, host="localhost", port=8000)