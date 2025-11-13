usersList = list()
for i in range(5):
    usersList.append(float(input(f"Number {i+1}: ")))
biggestNumber = max(usersList)
usersList.remove(biggestNumber)
biggestNumber = max(usersList)
index = usersList.index(biggestNumber)
resultList = [biggestNumber, index]
print(resultList)