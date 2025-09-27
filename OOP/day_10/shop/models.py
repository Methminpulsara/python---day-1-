import datetime
import time
from dataclasses import dataclass, field
from typing import List



class SuperMarketException(Exception):
    pass


@dataclass
class Product:
    product_id: str
    name: str
    price: float
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


@dataclass
class Customer:
    customer_id: str
    customer_name: str
    email: str
    contact: str


@dataclass
class OrderItem:
    product_id: str
    product_name: str
    quantity: int
    unit_price: float

    def total_price(self) -> float:
        return self.quantity * self.unit_price



@dataclass
class OrderItem:
    item_id: str
    quantity: int


@dataclass
class Order:
    order_id: str
    customer_id: str
    customer_name: str
    order_items: List[OrderItem] = field(default_factory=list)
    created_at: datetime.datetime = field(default_factory=datetime.datetime.now)

    def add_item(self , order_item : OrderItem):
        self.order_items.append(order_item)

    def total_price(self )->float:
        return sum([item.total_price() for item in self.order_items])

