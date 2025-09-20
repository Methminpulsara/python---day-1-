from user import User
from currunt_account import CurrentAccount
from account import Account
accounts : list[Account] = []
users : list[User] = []

def create_user(nic, name, contact):
    user = User(nic, name, contact)
    users.append(user)
    print(f"User created: {user}")
    return user


def find_user(user_nic):
    for user in users:
        if user.get_nic() == user_nic:
            return user

def find_accout(account_no):
    for acc in accounts:
        if acc.acc_no == account_no:
            return acc
def all_users():
    for user in users:
        print("helo")
        print(f"""
            User Name : {user.get_name()}
            Nic :  {user.get_nic()}
            Contact : {user.get_contact()}
        """)

def list_accounts():
    for account in accounts:
        print(f"""
        Account No: {account.acc_no}
        Balance : {account.balance}
        Branch : {account.branch}
        User name : {account.user.get_name()}
        """)
def deposit(self, amount):
    if amount <= 0:
        print("amount must be greater than 0.")
        return
    self.balance += amount
    print(f"{self.user.get_name()} deposited {amount}. New Balance: {self.balance}")

while True:
    print("""
       1) press 1 to create User 
       2) press 2 to create Account 
       3) press 3 to Show All Users  
       4) press 4 to Show Accounts
       5) press 5 to Deposit Money 
    """)

    choice = input("Enter Your choice : ")

    if choice == "1":
        nic = input("Enter Your nic number : ")
        name = input("Enter your name : ")
        contact = input("Enter your contact number : ")
        user = User(nic , name , contact)
        users.append(user)


    if choice == "2":
        account_no = input("Enter Your Account number : ")
        balance = input("Enter Your balance : ")
        branch = input("Enter Your branch : ")
        user_nic = input("Enter Your Nic : ")

        user_nic = find_user(user_nic)

        if user is not None:
            account_type = input("Enter Account Type ? saving/current")

            if account_type == "current":
                currunt_account = CurrentAccount(account_no , balance , branch , user ,[])
                accounts.append(currunt_account)
                print("Account Created ! ")


    if choice == "3":
        all_users()

    if choice == "4":
        list_accounts()

    if choice == "5":
        acc_no = input("Enter Your Account Number : ")
        account = find_accout(acc_no)

        if account is not None:
            amount = float(input("Enter amount to deposit : "))
            account.deposit(amount)
        else:
            print("Account not found.")

