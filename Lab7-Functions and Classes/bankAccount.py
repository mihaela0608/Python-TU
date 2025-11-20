class BankAccount:
    def __init__(self, accountNumber, person):
        self.accountNumber = accountNumber
        self.person = person
        self.balance = 0
    def add(self, money):
        self.balance+=money
    def withdrow(self, money):
        if(self.balance >= money):
            self.balance-=money
        else:
            print("Not enough money!")
    def display_balance(self):
        print(f"Balance: {self.balance}")

first = BankAccount(121425007, "Ivana")
second = BankAccount(121225852, "Georgi")

first.add(300)
second.add(400)
first.add(400)
second.withdrow(500)
first.withdrow(100)

first.display_balance()
second.display_balance()
    
