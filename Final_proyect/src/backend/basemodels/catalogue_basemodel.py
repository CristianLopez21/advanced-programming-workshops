"""This class represents"""
from pydantic import BaseModel
from .product_basemodel import Product

class Catalogue(BaseModel):
    """This class represent a base model catalogue of products"""
    id_catalogue: str

    @classmethod
    def show_list_products(cls):
        """This method is used to show a list of products
        

        Returns: 
            -A list of products.
            
        """
        return cls.products

    @classmethod
    def show_products_by_name(cls, name: str):
        """This method is used to search a product by name
        
        Args: 
        
            -name(str): The name of the product to show.
        
        Returns:  
            -A product filtered by name.





        """
        return [product for product in cls.products if product.name == name]

    @classmethod
    def show_products_by_department(cls, department: str):
        """This method is used to search a product by department
         Args: 
        
            -department (str): The department of the product to show.
        
        Returns:  
            -A product filtered by department.
        """

        return [
            product for product in cls.products if product.department == department
        ]

    @classmethod
    def add_product(cls, product: Product):
        """This method is used to add a product to the product list.
        Args: 
        
            -product(Product): A product.
        """
        cls.products.append(product)

    @classmethod

    def get_product(cls, id:str) -> Product:
        """This method is used to get a product
        Args: 
        
            -id (str): The id of the product to get.
        
        Returns:  
            -A product filtered by the id.
        
        """
        for product in cls.products:
            if product.id == id:
                return product
        return None    
