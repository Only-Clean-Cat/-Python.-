import threading
class BankAccount(threading.Thread):

    def __init__(self, account, amount, *args, **kwargs):
        super(BankAccount, self).__init__(*args, **kwargs)
        self.amount = amount
        self.account = account
        self.my_balance = 1_000

    def deposit_task(self, *args, **kwargs):
        super(BankAccount, self).__init__(*args, **kwargs)
        for _ in range(5):
            self.my_balance += self.amount
            print(f'Deposited {self.amount}, new balance is {self.my_balance}')
        return self.my_balance
    def withdraw_task(self,  *args, **kwargs):
        super(BankAccount, self).__init__(*args, **kwargs)
        for _ in range(5):
            self.my_balance -= self.amount
            print(f'Withdrew {self.amount}, new balance is {self.my_balance}')
        return self.my_balance
deposit_thread = threading.Thread(target=BankAccount.deposit_task, args=(100))
withdraw_thread = threading.Thread(target=BankAccount.withdraw_task, args=(150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
