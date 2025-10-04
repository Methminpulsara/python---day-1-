from typing import List, Dict

from day_10.shop.repository.order_repository import OrderRepository
from day_10.shop.models import Order


class InMemoryOrderRepository(OrderRepository):
    def __init__(self , filename:str = "orders.txt"):
        self.filename = filename

    def __save(self , orders:Dict[str:Order]):
        orders_dict = {}
    def add(self, order: Order) -> None:
        self.__orders[order.order_id] = order

    def get_by_id(self, order_id: str) -> Order:
        return self.__orders.get(order_id)

    def update(self, order: Order) -> None:
        self.__orders[order.order_id] = order

    def list_all_order(self) -> List[Order]:
        return list(self.__orders.values())
