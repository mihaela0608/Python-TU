import random

numbers = [random.randint(-10, 10) for k in range(10)]
for i in range(0, 11, 3):
    sum = numbers[i] + numbers[i+1]
    numbers.insert(i+1, sum)
numbers.insert(-1, numbers[-2] + numbers[-1])
print(numbers)