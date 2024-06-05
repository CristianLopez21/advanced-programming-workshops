"""This file has the classes that represents the catalogue of the plattform"""

from .product import Product


class Catalogue: 
    """This class represent a catalogue of products"""

    products = []

    def __init__(self, id_catalogo: str) -> None:
        self.id_catalogo = id_catalogo

    @classmethod
    def show_list_products(cls):
        """This method is used to show a list of products"""
        return cls.products

    @classmethod
    def show_products_by_name(cls, name: str):
        """This method is used to search a product by name"""
        return [product for product in cls.products if product.name == name]

    @classmethod
    def show_products_by_department(cls, department: str):
        """This method is used to search a product by department"""
        return [
            product for product in cls.products if product.department == department
        ]

    @classmethod
    def add_product(cls, product: Product, ):
        """This method is used to add a product to the vidogame list"""
        cls.products.append(product)

    @classmethod

    def get_product(cls, id:str) -> Product:
        """This method is used to get a product"""
        for product in cls.products:
            if product.id == id:
                return product
        return None