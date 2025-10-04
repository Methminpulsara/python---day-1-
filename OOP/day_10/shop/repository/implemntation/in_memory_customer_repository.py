from typing import List, Dict
import json

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

class FileSaveCustomerRepository(CustomerRepository):

    def __init__(self , filename:str = "customer.txt"):
        self.filename = filename

    def __save_customer(self  , customer: Dict[str:Customer]):
        customer_dict = {
            customer_id: {
                "product_id": product.product_id,
                "name": product.name,
                "price": product.price,
                "quantity": product.quantity
            }
            for customer_id, product in customer.items()
        }
        with open(self.filename, "w") as customer_file:
            json.dump(customer_dict, customer_file, indent=4)

    def __load_customer(self)-> Dict[str, Customer]:

        try:
            with open(self.filename, "r",) as f:
                data = json.load(f)
                return {
                    cid: Customer(
                        customer_id=cid,
                        customer_name=info
                    )
                    for cid, info in data.items()
                }
        except (FileNotFoundError, json.JSONDecodeError):
            return {}

    def get_by_id(self, customer_id: str) -> Customer:
        customers = self.__load_customer()
        return customers.get(customer_id)
    def update(self, customer: Customer) -> Customer:
        products = self.__load_customer()
        if customer.customer_id in products:
            products[customer.customer_id] = customer
            self.__save_customer(products)
        else:
            raise KeyError(f"Product with ID {customer.customer_id} not found.")

    def list_all_customer(self) -> List[Customer]:
        return list(self.__load_customer().values())
        pass

    def add(self, customer: Customer)-> None:
        pass
