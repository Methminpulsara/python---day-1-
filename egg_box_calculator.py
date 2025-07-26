number_of_eggs = int(input("Enter Number Of Eggs: "))

box = number_of_eggs // 12
remaining = number_of_eggs % 12
print(f"{box} box and {remaining} remaining eggs")

