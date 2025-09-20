from user import User

accounts = []
users = []

def create_user(nic, name, contact):
    user = User(nic, name, contact)
    users.append(user)
    print(f"User created: {user}")
    return user


while True:
    print("""
       1) press 1 to create User :
       2) press 2 to create Account :
    """)

    choice = input("Enter Your choice : ")

    if choice == "1":
        nic = input("Enter Your nic number : ")
        name = input("Enter your name : ")
        contact = input("Enter your contact number : ")
        create_user(nic, name, contact)
