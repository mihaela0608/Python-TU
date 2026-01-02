import random

n = 0

while True:
    try:
        n = int(input("Count of numbers: "))
        if(n <= 14 or n >= 55):
            raise ValueError
        break
    except ValueError:
        print("Invalid number")

a = random.randint(-3200, -1500)
b = random.randint(1800, 5200)

L1 = []

for i in range(n):
    while True:
        try:
            num = int(input(f"Number {i}: "))
            if(num > a and num <= b):
                L1.append(num)
                break
        except ValueError:
            continue

count1 = 0
for num in L1:
    check = abs(num) // 10 % 10
    if(check % 4 == 0):
        count1+=1

sum_n=0
count_n=0
for num in L1:
    if(abs(num) > 99 and abs(num) < 1000):
        if(num % 6 == 0):
            sum_n+=num
            count_n+=1

average_n = 0
if(count_n > 0):
    average_n = sum / average_n

L2 = []
for num in L1:
    if(abs(num) > 999 and abs(num) < 9999):
        if(num % 2 == 0):
            L2.append(num)

count_odd=0
for i in range(1, len(L2), 2):
    if(L2[i] % 2 != 0):
        count_odd+=1
for i in range(0, len(L2), 2):
    L2[i] = -11

if(len(L1) > len(L2)):
    if(len(L1) > 1):
        L1.pop(0)
        L1.pop()
elif(len(L2) > len(L1)):
    if(len(L2) > 1):
        L2.pop(0)
        L2.pop()
    