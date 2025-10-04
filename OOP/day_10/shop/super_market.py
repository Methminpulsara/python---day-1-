from day_10.shop.repository.implemntation.in_memory_order_repository import InMemoryOrderRepository
from day_10.shop.repository.implemntation.in_memory_customer_repository import InMemoryCustomerRepository
from day_10.shop.repository.implemntation.inMemoryProductRepository import InMemoryProductRepository
from day_10.shop.repository.implemntation.inMemoryProductRepository import FileSaveProductRepository

from day_10.shop.service.service import SupperMarketService, SuperMarketException


def print_menu():
    print("\nChoose an option:")
    print("1. Add Product")
    print("2. Add Customer")
    print("3. Create Order")
    print("4. Add Item to Order")
    print("5. List All Products")
    print("6. List Available Products")
    print("7. List All Customers")
    print("0. Exit")
    print("-" * 50)


product_repo = FileSaveProductRepository()
customer_repo = InMemoryCustomerRepository()
order_repo = InMemoryOrderRepository()

service = SupperMarketService()
service.products = product_repo
service.customer = customer_repo
service.order = order_repo


def main():
    while True:
        # print_header()
        print_menu()
        choice = input("Enter your choice: ")

        try:
            if choice == "1":
                add_product()

            elif choice == "2":
                add_customer()

            elif choice == "3":
                create_order()

            elif choice == "4":
                add_items_for_order()

            elif choice == "5":
                get_prodcts()

            elif choice == "6":
                get_available_products()
            elif choice == "7":
                get_all_customers()

            elif choice == "0":
                print("Exiting SuperMarket System...")
                break

            else:
                print("Invalid choice, please try again.")

        except SuperMarketException as e:
            print(f"Error: {e}")
        except Exception as e:
            print(f"Error: {e}")


def add_product():
    pid = input("Enter Product ID: ")
    name = input("Enter Product Name: ")
    price = float(input("Enter Price: "))
    qty = int(input("Enter Quantity: "))
    product = service.add_product(pid, name, price, qty)
    print(f"Product added: {product.name} ({product.quantity} /=)")


def add_customer():
    cid = input("Enter Customer ID: ")
    name = input("Enter Customer Name: ")
    email = input("Enter Email: ")
    contact = input("Enter Contact: ")
    customer = service.add_customer(cid, name, email, contact)
    print(f" Customer added: {customer.customer_name}")


def create_order():
    oid = input("Enter Order ID: ")
    cid = input("Enter Customer ID: ")
    order = service.add_order(oid, cid)
    print(f"Order created: {order.order_id}")


def add_items_for_order():
    oid = input("Enter Order ID: ")
    pid = input("Enter Product ID: ")
    qty = int(input("Enter Quantity: "))
    service.add_order_items(oid, pid, qty)
    print("Item added to order")


def get_prodcts():
    products = service.get_all_products()



def get_available_products():
    products = service.get_all_available_products()



def get_all_customers():
    customers = service.get_all_customers()


main()
