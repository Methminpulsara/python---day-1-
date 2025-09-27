from typing import List

from day_10.shop.repository.customer_repository import CustomerRepository
from day_10.shop.models import Customer


class InMemoryCustomerRepository(CustomerRepository):

    def __init__(self):
        self.__customer: Customer[str: Customer] = {}

    def add(self, customer: Customer) -> None:
        self.__customer[customer.customer_id] = customer

    def get_by_id(self, customer_id: str) -> Customer:
        return self.__customer.get(customer_id)

    def update(self, customer: Customer) -> None:
        self.__customer[customer] = customer

    def list_all_customer(self) -> List[Customer]:
        return list(self.__customer.values())
