import threading
class BankAccount(threading.Thread):

    def __init__(self, account, amount):
        self.amount = amount
        self.account = account
        self.my_balance = 1_000
        self.lock = threading.Lock()

    def deposit_task(self, account, amount):
        self.amount = amount
        self.account = account
        for _ in range(5):
            with self.lock:
                self.my_balance += self.amount
                print(f'Deposited {self.amount}, new balance is {self.my_balance}')
        return self.my_balance
    def withdraw_task(self, account, amount):
        self.amount = amount
        self.account = account
        for _ in range(5):
            with self.lock:
                self.my_balance -= self.amount
                print(f'Withdrew {self.amount}, new balance is {self.my_balance}')
        return self.my_balance
my_deposit = BankAccount('Dred', 100)
deposit_thread = threading.Thread(target=my_deposit.deposit_task, args=('Dred', 100))
withdraw_thread = threading.Thread(target=my_deposit.withdraw_task, args=('Dred', 150))

deposit_thread.start()
withdraw_thread.start()

deposit_thread.join()
withdraw_thread.join()
