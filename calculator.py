num1 = int(input("Enter first Number  : "))
num2 = int(input("Enter second Number : "))

operator = input("Enter Operation : ")



if operator == "+":
    print(f"{num1} + {num2} = ", num1+num2)
elif operator == "-":
    print(f"{num1} - {num2} = ", num1-num2)
elif operator == "*":
    print(f"{num1} * {num2} =", num1*num2)
elif operator == "/":
    if num2 > 0:
        print(f"{num1} / {num2} =", num1/num2)
    else:
        print("Can't be Divide  by 0")
elif operator == "//":
    print(f"{num1} // {num2} =", num1//num2)
elif operator == "%":
    print(f"{num1} % {num2} =", num1 % num2)
elif operator == "**":
    print(f"{num1} ** {num2} =", num1 ** num2)
else:
    print("Not Valid Operation")



# USING MATCH
# match operator:
#     case "+":
#         print(f"{num1} + {num2} = {num1 + num2}")
#     case "-":
#         print(f"{num1} - {num2} = {num1 - num2}")
#     case "/":
#         if num2 != 0:
#             print(f"{num1} / {num2} = {num1 / num2}")
#         else:
#             print("can't be Divide by 0")
#     case "*":
#         print(f"{num1} * {num2} = {num1 * num2}")
#     case "**":
#         print(f"{num1} ** {num2} = {num1 ** num2}")
#     case "%":
#         print(f"{num1} % {num2} = {num1 % num2}")