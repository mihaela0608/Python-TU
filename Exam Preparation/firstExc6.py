import random

k = 0

while True:
    try:
        k = int(input("Count: "))
        if (k >= 60 or k <= 15):
            raise ValueError
        break
    except ValueError:
        print("Invalid count")
    
x = random.randint(-3500, -1800)
y = random.randint(2000, 5500)

arr_1 = []

for i in range(k):
    while True:
        num = int(input(f"Number {i}: "))
        if(num > x and num <= y):
            arr_1.append(num)
            break
        else:
            print("Invalid number")

count_negative = 0
for i in arr_1:
    if(i < 0):
        num = i // 100
        if(num % 10 % 2 == 1):
            count_negative+=1

count_avg = 0
sum_avg = 0
average = 0
for i in arr_1:
    if(len(str(abs(i))) == 3):
        if i % 7 == 0:
            count_avg+=1
            sum_avg+=i

if(count_avg > 0):
    average = sum_avg / count_avg

arr_2 = []
for i in arr_1:
    if(len(str(abs(i))) == 4):
        if(i % 5 == 0):
            arr_2.append(i)

count_even = 0
for i in range(1, len(arr_2), 2):
    if(i % 2 == 0):
        count_even+=1

for i in range(0, len(arr_2), 2):
    arr_2[i]= -21

l_1 = len(arr_1)
l_2 = len(arr_2)
if(l_1 > l_2):
    if(l_1 >= 2):
        arr_1.pop(0)
        arr_1.pop()
elif(l_2 > l_1):
    if(l_2 >= 2):
        arr_2.pop(0)
        arr_2.pop()


