def check_age(age):
    if age <= 0 :
        raise ValueError("Age cannot be less than zero")
    print("Your age is" , age)

# try:
#     age = int(input("Enter Your Age : "))
#     check_age(age)
# except ValueError as e:
#     print(e)
#
def divishion(num1 , num2):
    print(num1 / num2 )

try:
    divishion(5 , 0)
except ZeroDivisionError as e :
    print(e)

