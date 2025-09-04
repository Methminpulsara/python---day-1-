# phone_book = {}
#
# def add_contact():
#     name = input("Enter Your Name : ")
#     number = input("Enter Your Contact Number : ")
#
#     if name in phone_book:
#         phone_book[name].append(number)
#     else:
#         phone_book[name] = [number]
#
#     print(f"Added {number} for {name}")
#
# def view_contact():
#     name = input("Enter Your name : ")
#     if name in phone_book:
#         print("Your Contact numbers  :" , phone_book[name])
#     else:
#         print("Not found in Phone Book !")
#
# def delete_contact():
#     name = input("Enter You name To Delete Contact : ")
#
#     if name in phone_book:
#         del phone_book[name]
#         print(f"Contact Deleted ! {name}")
#
# def all_contacts ():
#     print("All contacts ")
#
#
# def main():
#     while True:
#         print("\n--- Phone Book Menu ---")
#         print("1. Add Contact")
#         print("2. View Contact")
#         print("3. Delete Contact")
#         print("4. View All Contacts")
#         print("5. Exit")
#
#         choice = input("Enter your choice: ")
#
#         if choice == "1":
#             add_contact()
#         elif choice == "2":
#             view_contact()
#         elif choice == "3":
#             delete_contact()
#         # elif choice == "4":
#         #     view_all_contacts()
#         elif choice == "5":
#             print("Exiting Phone Book. Bye!")
#             break
#         else:
#             print("Invalid choice, try again.")
#
# main()
for i in range(3):
    print(i)