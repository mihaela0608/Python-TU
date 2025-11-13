class BankAcc:
    def __init__(self, number, money):
        self.number = number
        self.money = money
    def addMoney(self, moneyForAdding):
        self.money+=moneyForAdding
    def lostPfMoney(self, moneyForLose):
        if (self.money >= moneyForLose):
            self.money-=moneyForLose
        else:
            print("Not enough money")

class SavingsAcc(BankAcc):
    def __init__(self, number, money, increase):
        super().__init__(number, money)
        self.increase = increase
    def addToBalance(self):
        self.money = (self.money * self.increase / 10) + self.money
    def info(self):
        return f"Savings account with number {self.number} has {self.money} leva with interst rate: {self.increase}"
    
class CheckingAcc(BankAcc):
    def __init__(self, number, money, tax):
        super().__init__(number, money)
        self.tax = tax

    def getMoney(self, moneyForGet):
        if(self.money > moneyForGet + self.tax):
            self.money-=moneyForGet + self.tax
        else:
            print("Not enough money")



