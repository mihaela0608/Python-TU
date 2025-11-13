import random

first = [random.randint(-20, 20) for i in range(5)]
second = [random.randint(-20, 20) for i in range(5)]

finalList = []

for i in range(5):
    finalList.append(first[i])
    finalList.append(second[i])

print(finalList)

