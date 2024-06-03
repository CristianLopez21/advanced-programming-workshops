from pydantic import BaseModel

class UserCredentials(BaseModel):
    user_email: str
    password: str