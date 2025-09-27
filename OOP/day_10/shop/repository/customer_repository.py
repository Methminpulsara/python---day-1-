from abc import ABC, abstractmethod
from typing import List

from ..models import Customer


class CustomerRepository:

    @abstractmethod
    def add(self, customer: Customer) -> None:
        pass

    @abstractmethod
    def get_by_id(self, customer_id: str) -> Customer:
        pass

    @abstractmethod
    def update(self, customer: Customer) -> Customer:
        pass

    @abstractmethod
    def list_all_customer(self) -> List[Customer]:
        pass
