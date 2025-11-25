def sumOfLists(list1, list2):
    sum = 0

    firstLenght = len(list1)
    secondLenght = len(list2)
    
    if(firstLenght > secondLenght):
        biggerList = list1
        smallerList = list2
    else:
        biggerList = list2
        smallerList = list1

    for i in range(len(smallerList)):
            sum+= biggerList[i] * smallerList[i]

    others = len(biggerList) - len(smallerList)
    if(others > 0):
        newCounter = 0
        for i in range(others + 1, len(biggerList)):
            sum+= biggerList[i] * smallerList[newCounter]
            newCounter+=1
        

    print(sum)

list1 = [1, 8, 2]
list2 = [2, 3]
sumOfLists(list1, list2)

