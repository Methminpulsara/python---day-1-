from typing import List

from day_10.shop.models import Order
from abc import ABC, abstractmethod


class OrderRepository(ABC):

    @abstractmethod
    def add(self, order: Order) -> None:
        pass

    @abstractmethod
    def get_by_id(self, order_id: str) -> Order:
        pass

    @abstractmethod
    def update(self, order: Order) -> None:
        pass

    @abstractmethod
    def list_all_order(self) -> List[Order]:
        pass

