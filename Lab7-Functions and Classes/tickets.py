all = 0
sales = 0
money = 0

def moneyFromSale(sale):
    global all
    global money
    row = int(sale.split(" -> ")[0])
    tickets = int(sale.split(" -> ")[1])
    all+=tickets
    if(row <= 3):
        money+= tickets * 20
    else:
        money+= tickets * 15


for i in range(3):
    info = input().split(", ")
    for sale in info:
        sales=sales + 1
        moneyFromSale(sale)
        


print("Sales: ", sales)
print("Theatre tickets: ", all)
print("Money: ", money)
    

