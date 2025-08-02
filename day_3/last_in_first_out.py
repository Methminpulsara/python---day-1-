numbers = []

for i in range(20):
    numbers.append(i)

print('Numbers after appending                => ', numbers)

numbers.pop()
print("After pop without index                => " , numbers)

numbers.pop(1)
print("After pop with index   (1)             => " , numbers)

numbers.remove(2)
print("Remove the first occurence in the list => " , numbers)


if 0 in numbers:
    print("List eka athule thiyend chek krnn puluwan apita one value ekk =>  yes")