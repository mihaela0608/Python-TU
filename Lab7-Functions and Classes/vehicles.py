class Vehicle:
    def __init__(self, tires, model, color):
        self.tires = tires
        self.model = model
        self.color = color
    def info(self):
        print(f"Number of tires: {self.tires}, Model: {self.model}, Color: {self.color}")
    
class LuxCar(Vehicle):
    def __init__(self, tires, model, color, passengers):
        super().__init__(tires, model, color)
        self.passengers = passengers
    def info(self):
        super().info()
        print("Passengers: ", self.passengers)
        
class SportsCar(Vehicle):
    def __init__(self, tires, model, color, loadlimit):
        super().__init__(tires, model, color)
        self.loadlimit = loadlimit
    def info(self):
        super().info()
        print("Loadlimit: ", self.loadlimit)

luxCar = LuxCar(4, "Lamborgini", "Pink", 5)
sportsCar = SportsCar(4, "Toyota", "red", 4)

luxCar.info()
sportsCar.info()

