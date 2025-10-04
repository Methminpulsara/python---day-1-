import time


# def number_genarator():
#     yield 10
#     yield 20
#
# for i in number_genarator():
#     print(i)

# def get_even_number():
#     currunt =0
#     while True:
#         currunt += 2
#         yield currunt
#
# even = get_even_number()
#
# for i in get_even_number():
#     print(i)

even_num_arr = [num for num in range(100) if num %2 == 0]
# print(even_num_arr)


even_num_gen = (num for num in range(100) if num % 2 == 0)
print(even_num_gen)

print(next(even_num_gen))