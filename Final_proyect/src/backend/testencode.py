from users_basemodel import UserCredentials, Admin
from db_connection import session, admins, products, SportFit
from product_basemodel import SportsFitness
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import IntegrityError

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
