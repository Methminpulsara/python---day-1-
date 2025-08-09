print("""
        Don't Copy Array Like this
        """)
numbers = [1, 2 , 3]

numbers_copy = numbers

numbers_copy[0] = 78

print(numbers)


print("""
        Don't Copy Array Like this
        """)
numbers_1 = [1, 2 , 3]

numbers_copy_1 = numbers[:]  # before  : => where want to start copy   # after : => where you want to stop copy

numbers_copy_1[0] = 100

print(numbers_1)