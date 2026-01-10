import random
n = 0
while True:
    try:
        n = int(input("Count: "))
        if n <= 15 or n >= 35:
            raise ArithmeticError("Number shoud be between 15 and 35")
        break
    except ValueError:
        print("Invalid data")
    except ArithmeticError as err:
        print(err)

l1 = []
for i in range(n):
    l1.append(random.randint(30, 300))

count_3 = 0
for num in l1:
    check = num // 10
    if (check % 10) % 3 == 0:
        count_3+=1

min_index = -1
min_value = 0
for i in range(0, len(l1), 1):
    if l1[i] % 6 == 4:
        if(min_index == -1):
            min_index = i
            min_value = l1[i]

l2 = [x for x in l1 if len(str(abs(x))) == 2 and (x % 2 == 0 or x % 3 == 0)]

average = 0
sum_avg = 0
count_avg = 0
for i in range(1, len(l2), 2):
    sum_avg+=l2[i]
    count_avg+=1

if(count_avg > 0):
    average = sum_avg / count_avg

min_num = 301
for num in l2:
    if num % 2 == 0 and num < min_num:
        min_num = num

l2.remove(min_num)

    