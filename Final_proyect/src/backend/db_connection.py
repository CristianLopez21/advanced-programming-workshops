"""This file is a module with the connection to the database of the project"""

import os
from sqlalchemy import create_engine, MetaData, Table, Column, Integer, String, Float
from sqlalchemy.orm import sessionmaker
from dotenv import load_dotenv

load_dotenv()
engine = create_engine(
    f"postgresql://{os.getenv('DB_USER')}:{os.getenv('DB_PASSWORD')}@{os.getenv('DB_URL')}:{os.getenv('DB_PORT')}/{os.getenv('DB_NAME')}"
)
Session = sessionmaker(bind=engine)
session = Session()
metadata = MetaData()
admins = Table("admins",
                metadata,
                Column("id", Integer, primary_key=True, autoincrement=True),
                Column("userName", String),
                Column("phone", String, default="No available"),
                Column("userEmail", String),
                Column("password", String),
                Column("access", String, default=True),
                )

customers = Table("customers",
                  metadata,
                  Column("id", Integer, primary_key=True, autoincrement=True),
                  Column("userName", String),
                  Column("phone", String, default="No available"),
                  Column("userEmail", String),
                  Column("password", String),
                  Column("access", String, default=False),
                  Column("addresdb", String, default="No selected"),
                  )

shoppinghist = Table("shoppingHistory",
                     metadata,
                     Column("id", Integer, primary_key=True, autoincrement=True),
                     Column("date", String),
                     Column("products", String),
                     Column("total", Float),
                     )

products = Table("products",
                 metadata,
                 Column("id", Integer, primary_key=True, autoincrement=True),
                 Column("name", String ),
                 Column("price", Float),
                 Column("stock", Integer),
                 Column("department", String),
                 Column("description", String),
                 Column("color", String),
                 Column("style", String),
                 )

fashion = Table("fashionproduct",
                metadata,
                Column("department", String, primary_key=True),
                Column("fabricType", String),
                Column("care", String),
                Column("originCountry", String),
                Column("size", String),
                Column("neckStyle", String),
                Column("soleMAterial", String),
                Column("outerMaterial", String),
                )

SportFit = Table("sportFitness",
                 metadata,
                 Column("size", String),
                 Column("Weight", String),
                 Column("materials", String),
                 Column("dimensions", String),
                 Column("useFor", String),
                 Column("ageRange", String),
                 )

homekitchen = Table("homeKitchen",
                    metadata,
                    Column("size", String),
                    Column("brand", String),
                    Column("dimensions", String),
                    Column("shape", String),
                    Column("units", String),
                    Column("capacity", String),
                    Column("specialFeature", String),
                    Column("uses", String),
                    Column("material", String),
                    )

Camera = Table("cameraphoto",
               metadata,
               Column("type", String),
               Column("brand", String),
               Column("modelname", String),
               Column("operatinSystem", String),
               Column("Connectivity", String),
               Column("imageResolution", String),
               Column("photoSensor", String),
               Column("imagestabilization", String),
               Column("shutterspeed", String),
               )

phone = Table("phone",
               metadata,
               Column("type", String),
               Column("brand", String),
               Column("modelname", String),
               Column("operatinSystem", String),
               Column("Connectivity", String),
               Column("wirelesscarrier", String),
               Column("memorystorage", String),
               Column("screensize", String),
               Column("batteryrating", String),
               )

headphone = Table("headphone",
               metadata,
               Column("type", String),
               Column("brand", String),
               Column("modelname", String),
               Column("operatinSystem", String),
               Column("Connectivity", String),
               Column("formfactor", String),
               Column("noisecancellation", String),
               )

console = Table("consoleAccesories",
               metadata,
               Column("type", String),
               Column("brand", String),
               Column("modelname", String),
               Column("operatinSystem", String),
               Column("Connectivity", String),
               Column("platform", String),
               Column("edition", String),
               Column("includecomponents", String),
               Column("compatibledevices", String),
               Column("memorystorage", String),
               )

videogame = Table("videogame",
               metadata,
               Column("type", String),
               Column("brand", String),
               Column("modelname", String),
               Column("operatinSystem", String),
               Column("Connectivity", String),
               Column("platform", String),
               Column("edition", String),
               Column("clasification", String),
               )

laptop = Table("laptop",
               metadata,
               Column("type", String),
               Column("brand", String),
               Column("modelname", String),
               Column("operatinSystem", String),
               Column("Connectivity", String),
               Column("capacity", String),
               Column("screensize", String),
               Column("harddisksize", String),
               Column("cpu", String),
               Column("ramMemory", String),
               Column("graphicCard", String),
               )

metadata.create_all(engine)
