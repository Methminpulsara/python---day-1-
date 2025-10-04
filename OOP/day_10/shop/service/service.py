from typing import List
from day_10.shop.models import Product, Customer, Order, OrderItem
from day_10.shop.repository.product_repository import ProductRepository
from day_10.shop.repository.customer_repository import CustomerRepository
from day_10.shop.repository.order_repository import OrderRepository


class SuperMarketException(Exception):
    pass


class SupperMarketService:
    products: ProductRepository
    customer: CustomerRepository
    order: OrderRepository

    # --- Products ---
    def add_product(self, product_id: str, name: str, price: float, quantity: int) -> Product:
        if not product_id.strip():
            raise SuperMarketException("Product ID cannot be empty")
        if self.products.get_by_id(product_id) is not None:
            raise SuperMarketException(f"Product with ID '{product_id}' already exists")
        if price <= 0:
            raise SuperMarketException("Price must be greater than zero")
        if quantity < 0:
            raise SuperMarketException("Quantity cannot be negative")

        product = Product(product_id=product_id, name=name, price=price, quantity=quantity)
        self.products.add(product)
        return product

    def get_all_products(self) -> List[Product]:
        return self.products.list_all_products()

    def get_all_available_products(self) -> List[Product]:
        return [p for p in self.products.list_all_products() if p.is_available()]

    # --- Customers ---
    def add_customer(self, cus_id: str, name: str, email: str, contact: str) -> Customer:
        if not cus_id.strip():
            raise SuperMarketException("Customer ID cannot be empty")
        if self.customer.get_by_id(cus_id) is not None:
            raise SuperMarketException(f"Customer with ID '{cus_id}' already exists")
        if not name.strip():
            raise SuperMarketException("Customer name cannot be empty")
        if "@" not in email:
            raise SuperMarketException("Invalid email address")
        if not contact.isdigit():
            raise SuperMarketException("Contact number must contain only digits")

        customer = Customer(customer_id=cus_id, customer_name=name, email=email, contact=contact)
        self.customer.add(customer)
        return customer

    def get_all_customers(self) -> List[Customer]:
        return self.customer.list_all_customer()

    # --- Orders ---
    def add_order(self, or_id: str, cus_id: str) -> Order:
        if self.order.get_by_id(or_id) is not None:
            raise SuperMarketException(f"Order with ID '{or_id}' already exists")

        customer = self.customer.get_by_id(cus_id)
        if customer is None:
            raise SuperMarketException("Customer does not exist")

        order = Order(order_id=or_id, customer_id=cus_id, customer_name=customer.customer_name)
        self.order.add(order)
        return order

    def add_order_items(self, ord_id: str, pro_id: str, quantity: int):
        order = self.order.get_by_id(ord_id)
        product = self.products.get_by_id(pro_id)

        if order is None:
            raise SuperMarketException("Order does not exist")
        if product is None:
            raise SuperMarketException("Product does not exist")
        if product.quantity < quantity:
            raise SuperMarketException("Stock not available")

        # Create order item
        order_item = OrderItem(product_id=pro_id, product_name=product.name,
                               quantity=quantity, unit_price=product.price)
        order.items.append(order_item)

        # Update product stock
        product.quantity -= quantity

        # Update repositories
        self.order.update(order)
        self.products.update(product)

    def get_all_orders(self) -> List[Order]:
        return self.order.list_all_order()
