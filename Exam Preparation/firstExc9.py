import random
n = 0
while True:
    try:
        n = int(input("Count: "))
        if n <= 20 or n >= 40:
            raise ArithmeticError("Count should be between 20 and 40")
        break
    except ValueError:
        print("Invalid count")
    except ArithmeticError as err:
        print(err)

l1 = []
for i in range(n):
    l1.append(random.randint(2, 200))

l1.remove(min(l1))

sum_even = 0
for i in range(0, len(l1), 2):
    sum_even+=l1[i]

count_0 = 0
for num in l1:
    if num % 10 == 0:
        count_0+=1

l2 = []
for num in l1:
    if (num % 3 == 0 and num % 4 != 0) or (num % 4 == 0 and num % 3 != 0):
        l2.append(num)

average = 0
sum_avg = 0
count_avg = 0
for num in l2:
    if num % 2 != 0:
        count_avg+=1
        sum_avg+=num

if(count_avg > 0):
    average = sum_avg / count_avg
max_index = l2.index(max(l2))