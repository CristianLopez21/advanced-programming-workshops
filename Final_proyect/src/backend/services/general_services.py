"""Doc string """
import uvicorn
from fastapi import FastAPI
from n_class import Catalogue
from basemodels import Product
from basemodels import User, Customer, Admin, UserCredentials

app = FastAPI()

#Users

@app.post("/login", response_model=User)
def login(credentials: UserCredentials):
    """This Function"""
    #TODO add to DB
    return User.login(credentials.user_email, credentials.password)

@app.post ("/create_customer")
def create_customer(customer: Customer):
    """This"""
    #TODO add to DB
    pass

@app.post("/create_admin")
def create_admin(admin: Admin):
    """This """
    #TODO add to DB
    pass

#------Customer------
@app.get("/show_history_get")
def show_history_get(user_email):
    """This """
    return Customer.show_history(user_email)

#------Admin------
@app.post("admin/add_product")
def add_product(product: Product):
    """This """
    Catalogue.add_product(product)


if __name__ == "__main__": 
    uvicorn.run(app, host="localhost", port=8000)
