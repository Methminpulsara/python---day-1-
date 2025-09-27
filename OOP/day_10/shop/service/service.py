
from day_10.shop.repository.implemntation.in_memory_order_repository import *
from day_10.shop.repository.implemntation.inMemoryProductRepository import *
from day_10.shop.repository.implemntation.in_memory_customer_repository import *

from day_10.shop.models import OrderItem


class SuperMarketException(Exception):
    pass


class SupperMarketService:
    products: ProductRepository
    customer: CustomerRepository
    order: OrderRepository

    def add_product(self, product_id: str, name: str, price: float, quantity: int) -> Product:
        # Validation
        if not product_id.strip():
            raise SuperMarketException("Product ID cannot be empty")

        if product_id in self.products:
            raise SuperMarketException(f"Product with ID '{product_id}' already exists")

        if price <= 0:
            raise SuperMarketException("Price must be greater than zero")

        if quantity < 0:
            raise SuperMarketException("Quantity cannot be negative")

        # Create product
        product = Product(product_id=product_id, name=name, price=price, quantity=quantity)
        self.products[product_id] = product
        return product

    def add_customer(self, cus_id: str, name: str, email: str, contact: str) -> Customer:
        # Validation
        if not cus_id.strip():
            raise SuperMarketException("Customer ID cannot be empty")

        if cus_id in self.customer:
            raise SuperMarketException(f"Customer with ID '{cus_id}' already exists")

        if not name.strip():
            raise SuperMarketException("Customer name cannot be empty")

        if "@" not in email:
            raise SuperMarketException("Invalid email address")

        if not contact.isdigit():
            raise SuperMarketException("Contact number must contain only digits")

        # Create customer
        customer = Customer(customer_id=cus_id, customer_name=name, email=email, contact=contact)
        self.customer[cus_id] = customer
        return customer

    def add_order(self, or_id: str, cus_id: str) -> Order:
        if self.order.get_by_id(order_id=or_id) is not None:
            raise SuperMarketException("Order exists with this order id")

        customer = self.customer.get_by_id(cus_id)
        if customer is None:
            raise SuperMarketException("Customer exists")

        order = Order(order_id=or_id, customer_id=cus_id, customer_name=customer.customer_name)
        self.order.add(order)
        return order

    def add_order_items(self, ord_id: str, pro_id: str, quantity: int):
        order = self.order.get_by_id(order_id=ord_id)
        product = self.products.get_by_id(pro_id)

        if order is None:
            raise SuperMarketException("Order doesnt exists")
        if product is None:
            raise SuperMarketException("Product doesnt exists")
        if product.quantity < quantity:
            raise SuperMarketException("Stock not available")

        order_item = OrderItem(product_id=pro_id, product_name=product.name, quantity=quantity,
                               unit_price=product.price)

        self.add_order(order_item)
        product.reduce_quantity(quantity)

        self.order.update(order)
        self.products.update(product)

    def get_all_products(self):
        return self.products.list_all_products()

    def get_all_available_products(self) -> List[Product]:
        return [product for product in self.products.list_all_products() if product.is_available()]

    def get_all_customers(self) -> List[Customer]:
        return self.customer.list_all_customer()

    def get_all_orders(self) -> List[Order]:
        return self.order.list_all_order()
