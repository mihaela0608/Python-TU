class BankAccount:
    def __init__(self, account_number, name, balance):
        self.account_number = account_number
        self.name = name
        self.balance = float(balance)
    def deposit(self, d):
        self.balance+=d
    def withdrawing_money(self, w):
        if(self.balance >= w):
            self.balance-=w
        else:
            print("Not enough money!")
    def print_info(self):
        print(f"{self.name} with number {self.account_number} has {self.balance}")
account_list = []
for i in range(10):
    num = input("Acc number: ")
    name = input("Name: ")
    balance = float(input("Balance: "))
    account_list.append(BankAccount(num, name, balance))
def max_balance():
    max_b = 0
    acc = BankAccount()
    for a in account_list:
        if a.balance > max_b:
            max_b=a.balance
            acc = a
    return acc
def sort_by_name():
    names = [name for name.name in account_list]
    names.sort(reverse=True)
    for name in names:
        print(name)