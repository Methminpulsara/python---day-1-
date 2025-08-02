ticket_price = 1000

while True:

    age = int(input("Enter Your Age : "))
    height = float(input("Enter Your Height : "))

    if height < 1.2:
        print(" Not Eligible to Ride ")
        continue

    if age >= 60:
        discount = 0.60
        final_price = ticket_price * (1 - discount)

    elif age >= 18:
        discount = 0.20
        final_price = ticket_price * (1 - discount)

    else:
        discount = 0
        final_price = ticket_price

    print(f" Your Ticket Price is : {final_price}")

    yes_or_no = input("You want to Play yes_or_no ?  y/n:  ")
    if yes_or_no == "n":
        break

