from account import Account
class CurrentAccount(Account):

    def __init__(self, acc_no, balance, branch, user , cheque_ids):
        super().__init__(acc_no, balance, branch, user)
        self.cheque_ids = cheque_ids

    def add(self , id ):
        self.cheque_ids.append(id)

    def search_id(self , id):
        for ch in self.cheque_ids:
            if ch == id:
                return True
        return False

