import random

n = 0

while True:
    try:
        n = int(input("Count of numbers: "))
        if(n <= 12 or n >= 40):
            raise ArithmeticError
        break
    except ValueError:
        print("Invalid data!")
    except ArithmeticError as err:
        print(err)

x = random.randint(-1800, -899)
y = random.randint(1500, 3201)

lst1 = []
for i in range(n):
    try:
        num = int(input(f"Number {i}: "))
        if(num > x and num <= y):
            lst1.append(num)
            break
    except ValueError:
        print("Invalid data")

negative_odd = 0
for num in lst1:
    if(num < 0):
        check = num // 100
        if(check % 2 != 0):
            negative_odd+=1

sum_7 = 0
count_7=0
for num in lst1:
    if((num > 9 and num < 100) or (num < -9 and num > -100)):
        if(num % 7 == 0):
            sum+=num
            count_7+=1

average = 0
if(count_7 > 0):
    average = sum_7 / count_7

lst2 = []
for num in lst1:
    if((num > 999) or (num < -999)):
        if(num % 4 == 0):
            lst2.append(num)

even = 0
for num in range(1, len(lst2), 2):
    if(num % 2 == 0):
        even+=1

for i in range(0, len(lst2), 2):
    lst2[i] = -7


if(len(lst1) > len(lst2)):
    if(len(lst1) > 1):
        lst1.pop(0)
        lst1.pop()
elif(len(lst2) > len(lst1))
    if(len(lst2) > 1):
            lst2.pop(0)
            lst2.pop()

