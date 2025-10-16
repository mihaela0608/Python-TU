# Първа задача
count = int(input("count="))

max = 0
for i in range(1, count+1):
    number = float(input("number="))
    if number > max:
        max = number
print(max)