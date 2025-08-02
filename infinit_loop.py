while True:

    number_of_eggs = int(input("Enter Number Of Eggs: "))

    box = number_of_eggs // 12
    remaining = number_of_eggs % 12
    print(f"{box} box and {remaining} remaining eggs")

    yes_or_no = input("You want to Play yes_or_no ?  y/n:  ")
    if yes_or_no == "n":
        break
