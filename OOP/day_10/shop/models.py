from dataclasses import dataclass
import datetime
from typing import List, Type


class SuperMarketException(Exception):
    pass


@dataclass
class Product:
    product_id = str
    name = str
    price = float
    quantity: int

    def is_available(self) -> bool:
        return self.quantity > 0

    def __add__(self, amount: int) -> None:
        if amount < 0:
            raise SuperMarketException("Amount cannot be less than zero")
        self.quantity += amount

    def reduce_quantity(self, amount: int) -> None:
        if amount > self.quantity:
            raise SuperMarketException("amount is greater than our product Quantity")
        var = self.quantity - amount


@dataclass
class Customer:
    customer_id = str
    customer_name = str
    email = str
    contact = str


@dataclass
class OrderItem:
    product_id = str
    product_name = str
    quantity = int
    unit_price = float


@dataclass
class Order:
    order_id = str
    customer_id = str
    customer_name = str
    created_at = datetime
    order_items = List[OrderItem]
