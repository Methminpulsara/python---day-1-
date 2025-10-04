from typing import List, Dict
from day_10.shop.repository.product_repository import ProductRepository
from day_10.shop.models import Product
import json


class InMemoryProductRepository(ProductRepository):
    def __init__(self):
        # Correct type hint: Dict[str, Product]
        self.__products: Dict[str, Product] = {}

    def add(self, product: Product) -> None:
        self.__products[product.product_id] = product

    def get_by_id(self, product_id: str) -> Product | None:
        return self.__products.get(product_id)

    def update(self, product: Product) -> None:
        if product.product_id in self.__products:
            self.__products[product.product_id] = product
        else:
            raise KeyError(f"Product with ID {product.product_id} not found.")

    def list_all_products(self) -> List[Product]:
        return list(self.__products.values())

    def get_all_dict(self) -> Dict[str, Product]:
        """Helper method to get raw product dictionary (for saving to file)."""
        return self.__products


class FileSaveProductRepository(ProductRepository):
    def __init__(self, filename: str = "product.txt"):
        self.filename = filename

    def add(self, product: Product) -> None:

        products = self._load_all_products()
        products[product.product_id] = product
        self._save_to_file(products)

    def _save_to_file(self, products: Dict[str, Product]) -> None:
        product_dict = {
            product_id: {
                "product_id": product.product_id,
                "name": product.name,
                "price": product.price,
                "quantity": product.quantity
            }
            for product_id, product in products.items()
        }
        with open(self.filename, "w") as f:
            json.dump(product_dict, f, indent=4)

    def _load_all_products(self) -> Dict[str, Product]:

        try:
            with open(self.filename, "r",) as f:
                data = json.load(f)
                return {
                    pid: Product(
                        product_id=pid,
                        name=info["name"],
                        price=info["price"],
                        quantity=info["quantity"]
                    )
                    for pid, info in data.items()
                }
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def get_by_id(self, product_id: str) -> Product | None:
        products = self._load_all_products()
        return products.get(product_id)

    def update(self, product: Product) -> None:
        products = self._load_all_products()
        if product.product_id in products:
            products[product.product_id] = product
            self._save_to_file(products)
        else:
            raise KeyError(f"Product with ID {product.product_id} not found.")

    def list_all_products(self) -> List[Product]:
        return list(self._load_all_products().values())
