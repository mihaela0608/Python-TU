def toDecimal(number):
    numberList = list(str(number))[::-1]
    print(numberList)
    result = 0
    for i in range(len(numberList)):
        result+= int(numberList[i]) * (2 ** i)
    print(result)

toDecimal(1010)