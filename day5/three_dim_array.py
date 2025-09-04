three_dim = [
[['1', 'y' , 'x'] , ['1-2', 'y' , 'x']],
[['2', 'y' , 'x'] , ['2-2', 'y' , 'x']],
[['3', 'y' , 'x'] , ['3-2', 'y' , 'x']],
]
# print(three_dim[0])
# print(three_dim[0][1])
# print(three_dim[0][0][0])

for i in three_dim:
    for arr in i:
        for each in arr:
            print(each)
