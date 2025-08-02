
book_names = ['jungle book', 'Harry potter', 'Harry potter 2']
# print(book_names[1])
# #
# # for i in book_names:
# #     print(i)
#
# book_names[1] = "severance"
#
# print("updated list ", book_names)
#
# book_names[0] = book_names [2]
#
# print("afeter assing equal values ", book_names)
#
# print("length of list", len(book_names))
#
# #OUT OF BOUND ====>   print(book_names[10])
#
# book_names.append("modolduwa")
# print("after append", book_names)
#
# print("revered assces ", book_names[-2])


for book_name in book_names:
    if book_name == 'jungle book':
        continue
    else:
        print(book_name)


book_names.insert(0 , "Sherlock holmes")

print("after adding new item to index 0" ,book_names)
