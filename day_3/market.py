# ==========OPTION ONE===============

# is_member = input("Are you a member? (yes/no): ") == "yes"
#
# if is_member:
#     bill_value = float(input("Enter your bill value: "))
#     using_coupons = input("Are you using coupons? (yes/no): ") == "yes"
#     buying_vegetables = input("Are you buying vegetables? (yes/no): ") == "yes"
#
#     if bill_value > 5000 and not using_coupons and buying_vegetables:
#         bill_value *= 0.8
#         print("20% discount applied.")
#     else:
#         print("No discount applied.")
#
#     print(f"Final bill: {bill_value}")
# else:
#     print("Only members are eligible for a discount.")


#=====OPTION TWO==================================
is_member = input("Are you a member? (yes/no): ") == "yes"
bill_value = float(input("Enter your bill value: "))
using_coupons = input("Are you using coupons? (yes/no): ") == "yes"
buying_vegetables = input("Are you buying vegetables? (yes/no): ") == "yes"

is_eligibal  = (bill_value > 5000  and not using_coupons and not is_member and not buying_vegetables)

if is_eligibal:
    print (f"Your bill biscount  is {bill_value * 0.2}")
else :
    print("You have not discounts ! ")