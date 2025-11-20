class Building:
    def __init__(self, height, area, address):
        self.height = height
        self.area = area
        self.address = address
    def info(self):
        print(f"Height: {self.height}, Area: {self.area}, Address: {self.address}")
    

class House(Building):
    def __init__(self, height, area, address, floors, person):
        super().__init__(height, area, address)
        self.floors = floors
        self.person = person

    def info(self):
        super().info()
        print(f"Floors: {self.floors}, To: {self.person}")

    def biggest(houses):
        if(type(houses) != list):
            print("Invalid data!")
            return
        biggest = 0
        biggestHouse = ""
        for house in houses:
            data = house.height / house.floors
            if(data > biggest):
                biggest = data
                biggestHouse = house
        biggestHouse.info()
    
first = House(40, 5000, "St. Ivan Rilski", 8, "Dimitar")
second = House(30, 3000, "Example", 6, "Georgi")
third = House(20, 2000, "Another Example", 4, "Ivan")
first.info()

House.biggest([first, second, third])
House.biggest(5)

            

    
    