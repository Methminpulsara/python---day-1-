amount = float(input("Enter Principal Amount: "))
years = int(input("How many years?: "))
percentage = float(input("Enter Percentage: "))

if amount >= 0 and years > 0:
    interest = (amount * percentage * years) / 100
    total_amount = amount + interest
    print(f"interest : {interest}")
    print(f"Total Amount after {years} years: {total_amount}")
else:
    print("invalid")
