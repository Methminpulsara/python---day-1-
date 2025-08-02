c0 = int(input("Enter a positive number: "))

if c0 > 1:
    while c0 != 1:
        print(c0)
        if c0 % 2 == 0:
            c0 = c0 // 2
        else:
            c0 = 3 * c0 + 1
    print(c0)
else:
    print("invalid input ")
