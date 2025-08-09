
def print_name(firstname, lastname):
    print(f"Your name is {firstname} {lastname}")

def multiply(a , b ):
    return a * b

f_name = input("Enter you first name : ")
s_name = input("Enter you second name : ")

""" # type 1 """
print_name(f_name , s_name)

""" # type 2 """
print_name(lastname=s_name, firstname=f_name)




"""   Return value  """

result = multiply(10 , 10)
print(result)