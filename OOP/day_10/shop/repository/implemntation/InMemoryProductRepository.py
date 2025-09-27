from typing import List

from day_10.shop.repository.product_repository import ProductRepository
from day_10.shop.models import Product


class InMemoryProductRepository(ProductRepository):

    def __init__(self):
        self.__products: Product[str: Product] = {}

    def add(self, product: Product) -> None:
        self.__products[product.product_id] = product

    def get_by_id(self, product_id: str) -> Product:
        return self.__products.get(product_id)

    def update(self, product: Product) -> None:
        self.__products[product.product_id] = product

    def list_all_products(self) -> List[Product]:
        return list(self.__products.values())
