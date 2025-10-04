add = lambda x , y : x + y
print(add(1 , 4))


print((lambda x , y : x + y)(10  , 10) )

math_operators = {
    "addition" : lambda x, y : x + y ,
    "subtraction" : lambda x ,y : x - y
}

for key , val in math_operators.items():
    print(f"{key} -  {val(100 , 200)}")