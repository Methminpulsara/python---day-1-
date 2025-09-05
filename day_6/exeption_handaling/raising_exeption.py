def check_age(age):
    if age <= 0 :
        raise ValueError("Age cannot be less than zero")
    print("Your age is" , age)


try:
    age = int(input("Enter Your Age : "))
    check_age(age)
except ValueError as e:
    print(e)