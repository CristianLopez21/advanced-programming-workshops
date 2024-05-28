import uvicorn
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String
from sqlalchemy.orm import sessionmaker
from fastapi import FastAPI

app = FastAPI()


@app.get("/hello_ud")
def hello_ud():
    """This function Returns a welcome message str: 'Welcome to UD!'"""
    return "Welcome to UD!"


engine = create_engine('postgresql://postgres:1525@localhost:5432/public') #
Session = sessionmaker(bind=engine)
session = Session()

metadata = MetaData()
products = Table('products', metadata,
                 Column('id', Integer, primary_key=True),
                 Column('name', String),
                 Column('description', String))

#eliminar la segunda llamada de app = FastAPI


@app.get("/products")
def get_products():
    """This function This function defines a query to select
      all the records in the table (products), executes the
      query and then returns all the data obtained in this"""

    query = products.select()
    result = session.execute(query)
    products_ = result.fetchall() #change the name products to products_ in this line and the next
    return products_

@app.post("/products")
def create_product(name: str, description: str):
    """This function receives the parameters name and description of type str,
    and then through a query it enters the data obtained in the product table and
    returns a message (Product created successfully)"""

    query = products.insert().values(name=name, description=description)
    session.execute(query)
    session.commit()
    return {"message": "Product created successfully"}

if __name__ == "__main__":
    uvicorn.run(app, host="0.0.0.0", port=8000)
