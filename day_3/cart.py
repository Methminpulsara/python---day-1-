

prduct_array = ["orange", "mango", "apple"]
cart = []

while True :
    print("View All Products                   [1]")
    print("View Last Item in the Cart          [2]")
    print("Remove Last Item                    [3]")
    print("Clear Cart                          [4]")
    choose = int(input("\nPlease press numbers to countinue  :"))
    if choose == 0:
        break
    if choose == 1:
        while True:
            print(f"\nOUR PRODUCTS\n{prduct_array}")
            add_product = input("What product is you want to add to cart ?  ")
            if add_product in prduct_array:
                cart.append(add_product)
                print("Your product is added to the cart!")
            else:
                print("You selected an invalid product.")

            yes_or_no = input("\nDo you want to add another product : ")
            if yes_or_no == "no":
                break
            elif yes_or_no != "yes":
                print("invalid input.")
                break

    if choose ==2 :
        print("\nVIEW ONLY LAST PRODUCT ! ")
        if len(cart) >=1:
            print("\nLast Item in the cart ==>  " , cart[-1])
            print("\n")
        else:
            print("\nNot Have Any Products ! ")

    if choose == 3:
        while True:
            print("\nDROP LAST ITEM IN THE CART ! ")
            print(cart)
            anwser = input("\nDo you Want to Remove Last Item ?  ") == "yes"
            if anwser :
                cart.pop()
                print("\nYour Items is Removed ! ")
            yes_or_no = input("\nDo you want to Remove again  : ")
            if yes_or_no == "no":
                break
            elif yes_or_no != "yes":
                print("invalid input.")
                break

    if choose == 4 :
        cart.clear()
        print("\nYour Cart is Cleared ")


