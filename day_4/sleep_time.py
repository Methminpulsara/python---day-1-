anwser_arr = []
total_hours = 0

for days in range(1,8):
    anwser = int(input("Enter How many hours for today ?  : "))
    anwser_arr.append(anwser)
print(anwser_arr)

"""


# for hours in anwser_arr:
# #     total_hours += hours
# print(f"Average = {total_hours // len(anwser_arr)} ")

meekama sum funtion ek use krla kelima krnnth puluwn number array ekknm eke okkogem ekthuwa arn denw apit sum ek 
"""

print(f"Average = {sum(anwser_arr) // len(anwser_arr)} ")

arr = [hours for hours in anwser_arr if hours >= 8]
print(f"More than 8 hours   {len(arr)} days")