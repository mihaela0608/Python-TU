import random

n = 0

while True:
    try:
        n = int(input("Count of numbers: "))
        if(n >= 50 or n<=10):
            raise ArithmeticError("Count should be between 10 and 50")
        break
    except ArithmeticError as err:
        print(err)
    except ValueError:
        print("Invalid number")

a = random.randint(-2500, -1301)
b = random.randint(1111, 4445)

first_list = []
negative = 0
for i in range(n):
    while True:
        try:
            number = int(input(f"Number {i}: "))
            if(number >= a and number <= b):
                first_list.append(number)
                break
            else:
                print("Number is out of range")
        except ValueError:
            print("Invalid number!")
    
for number in first_list:
    if(number < 0):
        number_check = number // 10
        if(number % 4 == 0 or number % 5 == 0):
            negative+=1

sum_even = 0
count_even = 0
for number in first_list:
    if (len(str(number)) == 2 and number % 2 == 0):
        count_even+=1
        sum_even+=number

second_list = []
for i in first_list:
    if(len(str(i)) == 3 and i%3 == 0):
        second_list.append(i)

count_odd = 0
for num in range(0, len(second_list), 2):
    if(second_list[num] % 2 == 0):
        count_odd+=1

for num in range(1, len(second_list), 2):
    second_list[num] = 13


if(len(second_list) > len(first_list)):
    second_list.pop(0)
    second_list.pop(len(second_list) - 1)
elif(len(first_list) > len(second_list)):
    first_list.pop(0)
    first_list.pop(len(first_list) - 1)
    
