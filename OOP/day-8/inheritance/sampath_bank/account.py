from user import User

class Account:
    def __init__(self, acc_no, balance, branch, user: User):
        self.acc_no = acc_no
        self.balance = balance
        self.branch = branch
        self.user = user   # Account has a User - composition

    def deposit(self, amount):
        if amount <= 0:
            print("amount must be greater than 0.")
            return
        self.balance += amount
        print(f"{self.user.name} deposited {amount}. New Balance: {self.balance}")

    def withdraw(self, amount):
        if amount <= 0:
            print("amount must be greater than 0.")
        elif amount > self.balance:
            print(f"{self.user.name} cant withdraw.")
        else:
            self.balance -= amount
            print(f"{self.user.name} withdrew {amount}. New Balance: {self.balance}")

    def check_balance(self):
        print(f"{self.user.name}'s Account Balance: {self.balance}")
        return self.balance

    def __str__(self):
        return f"Account {self.acc_no} | Branch: {self.branch} | Owner: {self.user.name}"


user1 = User()
user1.set_nice("23424234v")
user1.set_name("Methmin")
user1.set_contact("0719189399")
acc1 = Account("123", 5000, "Horana Branch", user1)

print(acc1)
acc1.check_balance()
acc1.deposit(1500)
acc1.withdraw(2000)
acc1.withdraw(6000)  # insufficient
