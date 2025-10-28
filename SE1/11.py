count = int(input("Брой скиори:"))
sum = 0
for i in range(1, count+1):
    jackets = int(input(f"Брой якета скиор {i}:"))
    helmets = int(input(f"Брой каски скиор {i}:"))
    shoes = int(input(f"Брой Обувки скиор {i}:"))
    sum+= jackets * 120 + helmets * 75 + shoes * 299.90
sum = sum * 1.2
print(f"Sum: %.2f" %(sum))