class Market:
    def __init__(self, barcode, name, manufacturer, price, quantity):
        self.barcode = barcode
        self.name = name
        self.manufacturer = manufacturer
        self.price = float(price)
        self.quantity = float(quantity)
    def product_info(self):
        print(f"{self.name} with barcode {self.barcode} has been manufactures by {self.manufacturer}, cost {self.price} for {self.quantity}")
    def change_barcode(self):
        self.barcode = input("New barcode: ")
    def change_quantity(self):
        self.quantity = input("New quantity: ")
product_list = []
for i in range(3):
    barcode = input("Barcode: ")
    name = input("Name: ")
    manf = input("Manufacturer: ")
    price = input("Price: ")
    quantity = input("Quantity: ")
    product_list.append(Market(barcode, name, manf, price, quantity))

def search_by_barcode(product_list, barcode):
    for p in product_list:
        if p.barcode == barcode:
            p.product_info()
            break
def search_by_man(product_list, manufacturer):
    for p in product_list:
        if p.manufacturer == manufacturer:
            p.product_info()
def sell_product_by_name(product_list, name, num):
    for p in product_list:
        if p.name == name:
            if p.quantity >= num:
                print("Успешна продажба")
                p.quantity-=num
            else:
                print("Недостатъчна наличност")
         return
    print("Не е открит такъв продукт")
