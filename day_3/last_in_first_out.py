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

numbers.clear()
print("Whule list is cleared : ", numbers)



new_list = []

list_with_dups = [2, 2, 2, 6, 5, 7, 8, 8, 8, 8]

for number in list_with_dups:
    if number not in new_list:
        new_list.append(number)

print(" without duplicates:", new_list)
