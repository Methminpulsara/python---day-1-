class Account:
    print("Account Object")

    def __init__(self, acc_no, balance, branch, ):
        self.acc_no = acc_no
        self.balance = balance
        self.branch = branch

    def deposit(self):
        print("deposit , withdraw , chech balance")
