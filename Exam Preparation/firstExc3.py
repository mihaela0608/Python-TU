import random

n = 0

while True:
    try:
        n = int(input("Count of numbers: "))
        if(n <= 9 or n >= 45):
            raise ValueError
        break
    except ValueError:
        print("Invalid number")

p = random.randint(-2400, -1100)
q = random.randint(1300, 4100)

lstA = []

for i in range(n):
    while True:
        try:
            number = int(input(f"Number {i}: "))
            if(number <= q and number > p):
                lstA.append(number)
                break
        except ValueError:
            print("Invalid number")

count_3=0

for num in lstA:
    if(num < 0):
        check = (num // 10) % 10
        if(check % 3 == 0):
            count_3+=1

sum_n=0
count_n=0
for num in lstA:
    if((num > 9 and num < 100) or (num < -9 and num > -100)):
        if(num % 2 !+ 0):
            sum_n+=num
            count_n+=1

average = 0
if(count_n > 0):
    average = sum_n // count_n

lstB=[]
for num in lstA:
    if((num > 99 and num < 1000) or (num < -99 and num > -1000)):
        if(num % 5 == 0):
            lstB.append(num)

count_even = 0
for i in range(0, len(lstB), 2):
    if(lstB[i] % 2 == 0):
        count_even+=1
for i in range(1, len(lstB), 2):
    lstB[i] = 25


if(len(lstA) > len(lstB)):
    if(len(lstA) > 1):
        lstA.pop(0)
        lstA.pop()
elif(len(lstB) > len(lstA)):
    if(len(lstB) > 1):
        lstB.pop(0)
        lstB.pop()