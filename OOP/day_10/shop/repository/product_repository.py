from typing import List

from day_10.shop.models import Product
from abc import ABC, abstractmethod


class ProductRepository(ABC):

    @abstractmethod
    def add(self, product: Product) -> None:
        pass

    @abstractmethod
    def get_by_id(self, product_id: str) -> Product:
        pass

    @abstractmethod
    def update(self , product : Product) -> None:
        pass

    @abstractmethod
    def list_all_products(self) -> List[Product]:
        pass

