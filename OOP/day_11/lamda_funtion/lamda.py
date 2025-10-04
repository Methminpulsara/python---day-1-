add = lambda x , y : x + y
print(add(1 , 4))


print((lambda x , y : x + y)(10  , 10) )

math_operators = {
    "addition" : lambda x, y : x + y ,
    "subtraction" : lambda x ,y : x - y
}

for key , val in math_operators.items():
    print(f"{key} -  {val(100 , 200)}")


nums = [1 , 2 , 3 , 4 , 4 , 5, 6 , 6]


nams_doubled_map = list(map(lambda x : x * 2 , nums))
print("Doubled numbers -", nams_doubled_map)

filtered_nums = list(map(lambda x : x % 2 == 0 , nums))
print(filtered_nums)