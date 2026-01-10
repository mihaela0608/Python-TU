import random

n = 0

while True:
    try:
        n = int(input("Count: "))
        if (n <= 12 or n >= 50):
            raise ValueError
        break
    except ValueError:
        print("Invalid data for n")

m = random.randint(-4000, -2000)
n = random.randint(2500, 6000)

L1 = []

for i in range(n):

    while True:
        try:
            num = int(input(f"Number {i}: "))
            if (num < m or num > n):
                raise ValueError
            L1.append(num)
            break
        except ValueError:
            print("Invalid number")

count = 0
for num in L1:
    if (num < 0):
        n = (num // 10) % 10
        if (n % 5 == 0):
            count+=1

sum = 0
count2 = 0
average = 0
for num in L1:
    if (len(abs(num)) == 2):
        if(num % 3 == 0):
            sum+=num
            count2+=1

if count>0:
    average= sum / count

L2 = []

for num in L1:
    if(len(abs(num)) == 4):
        if num % 4 == 0:
            L2.append(num)

count3 = 0
for i in range (1, len(L2), 2):
    if(L2[i] % 2 == 0):
        count3+=1

for i in range(0, len(L2), 2):
    L2[i] = -9

if(len(L2) > len(L1)):
    if len(L2) >= 2:
        L2.pop(0)
        L2.pop()
elif(len(L1) > len(L2)):
    if len(L1) >= 2:
        L1.pop(0)
        L1.pop()
