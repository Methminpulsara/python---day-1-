from account import Account


class SavingAccount(Account):

    def __init__(self, acc_no, balance, branch, user, atm_number):
        super().__init__(acc_no, balance, branch, user)
        self.atm_number = atm_number

    def add_instres(self):
        self.balance += self.balance * 0.03
