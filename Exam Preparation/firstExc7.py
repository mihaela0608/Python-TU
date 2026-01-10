n = 0
while True:
    try:
        n = int(input("Count: "))
        if n <= 15 or n >= 35:
            raise ArithmeticError("The number should be between 15 and 35")
        break
    except ValueError:
        print("Invalid data")
    except ArithmeticError as err:
        print(err)

list1 = []

for i in range(n):
    while True:
        try:
            num = int(input(f"Number {i}: "))
            if num < 30 or num > 300:
                raise ArithmeticError("Number should be between 30 and 300")
            list1.append(num)
            break
        except ValueError:
            print("Invalid data")
        except ArithmeticError as err:
            print(err)

count_3 = 0

for i in list1:
    num = i // 10
    if num % 10 % 3 == 0:
        count_3+=1

min_index = -1
num_value = 0
for i in range(len(list1)):
    num = list1[i]
    if(num % 6 == 4):
        if(min_index == -1):
            min_index = i
            num_value = num
        elif(num < num_value):
            min_index = i
            num_value = num

list2 = []

for i in list1:
    if(len(str(abs(i))) == 2):
        if(i % 2 == 0 or i % 3 == 0):
            list2.append(i)

average = 0
count_odd = 0
sum_odd = 0
for i in range(1, len(list2), 2):
    count_odd+=1
    sum_odd+=list2[i]

if(count_odd > 0):
    average = sum_odd / count_odd

min_number = 1000
for i in list2:
    if i < min_number:
        min_number = i
list2.remove(min_number)
