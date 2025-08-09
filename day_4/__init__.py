numbers = [1 , 1 , 3 , 4, 6 , 7 , 8 , 9]

if numbers:
    for number in numbers:
        max_number = numbers[0]
        if number > max_number :
          max_number = number
    print(max_number)
else:
    print("numbers not in the array")

