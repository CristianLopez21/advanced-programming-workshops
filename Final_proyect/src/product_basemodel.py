from pydantic import BaseModel


class Product(BaseModel):
    """This class represent a baasemodel of a Product"""

    id: str
    name: str
    price: float
    stock: int
    department: str
    description: str
    color: str
    style: str

    def show_product(self):
        """This method is used to show a product.
        
        Returns: 
            -A product.
        


        """
        return self
