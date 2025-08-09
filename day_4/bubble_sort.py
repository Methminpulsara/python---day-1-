un_sorted_list = [7 , 1 , 6 , 9 , 5 , 2 , 7 , 8 , 0]

for i in range(len(un_sorted_list)-1):
   for x in range((len(un_sorted_list) - 1) - i):
       if un_sorted_list[x] > un_sorted_list[x + 1]:
           un_sorted_list[x], un_sorted_list[x + 1] = un_sorted_list[x + 1], un_sorted_list[x]
print(un_sorted_list)


