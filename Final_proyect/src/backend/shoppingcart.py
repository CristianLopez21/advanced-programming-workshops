from pydantic import BaseModel

class Shoppingcart(BaseModel):
    id_: int = None
    products: list
    total: float
