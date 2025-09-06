products = [{
    "id" : "1" ,
    "name" : "mango",
    "price" :150.00
},
{
    "id": "2",
    "name": "orange",
    "price": 150.00
}
]

def view_products():
    for prduct in products:
        print(f"ID - {prduct['id']} Name - {prduct['name']} Price- {prduct['price']}")

def add(product_id , name , price):
    for product in products:
        if product['id'] == product_id:
            return "Product is already have in the system"

    products.append({"id": product_id , "name" : name , "price" : price})
    return "Product Added !"

def find_producrt(product_id):
    for pr in products:
        if product_id == pr["id"]:
            return pr

def remove_product(product_id):
    for pr in products:
        if pr['id'] == product_id:
            print("Removed ! ")
add("3","bananana",120.00)
view_products()
print(find_producrt("1"))
remove_product("2")
view_products()