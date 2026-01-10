class BankAccount:
    def __init__(self, account_number, holder_name, balance=0):
        self.account_number = account_number
        self.holder_name = holder_name
        self.balance = float(balance)
    def account_info(self):
        print(f"{self.holder_name} with number {self.account_number} has {self.balance}")
    def change_bal(self):
        self.balance = float(input("New balance"))
    
accounts_list = []
for i in range(5):
    num = input()
    name = input()
    balance = float(input())
    acc = BankAccount(num, name, balance)
    accounts_list.append(acc)

def depposit(accounts_list, num, ammount):
    for a in accounts_list:
        if a.account_number == num:
            a.balance+=ammount
            break
def withdraw(accounts_list, num, ammount):
    for a in accounts_list:
        if a.account_number == num:
            if a.balance >= ammount:
                a.balance-=ammount
            else:
                print("Not enough money")
            break
def get_balance(accounts_list, num):
    for a in accounts_list:
        if a.account_number == num:
            return a.balance
def change_name(accounts_list, num, name):
    for a in accounts_list:
        if a.account_number == num:
            a.holder_name = name
            a.account_info()
            break


