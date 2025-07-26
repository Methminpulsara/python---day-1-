monthly = float(input("Enter your salary: "))
salary = monthly * 12

if salary <= 1200000:
    print("You don't need to pay tax!")
else:
    taxable = salary - 1200000
    tax = 0

    if taxable <= 500000:
        tax = taxable * 0.06
    elif taxable <= 1000000:
        tax = (500000 * 0.06) + ((taxable - 500000) * 0.12)
    elif taxable <= 1500000:
        tax = (500000 * 0.06) + (500000 * 0.12) + ((taxable - 1000000) * 0.18)
    elif taxable <= 2000000:
        tax = (500000 * 0.06) + (500000 * 0.12) + (500000 * 0.18) + ((taxable - 1500000) * 0.24)
    elif taxable <= 2500000:
        tax = (500000 * 0.06) + (500000 * 0.12) + (500000 * 0.18) + (500000 * 0.24) + ((taxable - 1500000) * 0.30)


    monthly= tax / 12

    print(f"You Have to Pay Tax = {tax/12}")
    print(f"you Have to Pay Monthly Tax : {monthly}")