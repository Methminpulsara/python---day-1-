from typing import List

from day_10.shop.repository.order_repository import OrderRepository
from day_10.shop.models import Order


class InMemoryOrderRepository(OrderRepository):
    def __init__(self):
        self.__orders: Order[str: Order] = {}

    def add(self, order: Order) -> None:
        self.__orders[order.order_id] = order

    def get_by_id(self, order_id: str) -> Order:
        return self.__orders.get(order_id)

    def update(self, order: Order) -> None:
        self.__orders[order.order_id] = order

    def list_all_order(self) -> List[Order]:
        return list(self.__orders.values())
