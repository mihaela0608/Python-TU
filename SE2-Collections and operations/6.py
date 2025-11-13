import random

count = int(input("Count: "))
ourList = [random.randint(-20, 20) for i in range(count)]
print(ourList)
evenIndex = [ourList[i] for i in range(len(ourList)) if i%2 == 0]
evenIndex.sort()
print(evenIndex)
oddIndex = [ourList[i] for i in range(len(ourList)) if i%2 != 0]
oddIndex.sort()
oddIndex = oddIndex[::-1]
print(oddIndex)