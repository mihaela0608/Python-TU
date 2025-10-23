number = str(input())
firstTup = tuple(int(digit) for digit in number)
print(firstTup)
secondTup = firstTup[::-1]
print(secondTup)
