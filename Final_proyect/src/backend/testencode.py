from users_basemodel import UserCredentials, Admin
from db_connection import session, admins
from fastapi import FastAPI
from fastapi.encoders import jsonable_encoder
from sqlalchemy.exc import IntegrityError

app = FastAPI()

@app.post("/items")
async def read_item(data: UserCredentials):
    try: 
        query_admins = admins.select().where(admins.c.userEmail == data.user_email, admins.c.password == data.password)
        result_admins = session.execute(query_admins).fetchone()

        if result_admins:
            return {"message": "Admin login successful", "user": result_admins}
        
    except IntegrityError as e:
        print(f"Error inserting data: {e}")
        session.rollback()

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