def pald(num):
    number = str(num)
    reversedNumber = number[::-1]
    if (number == reversedNumber):
        return True
    else:
        return False
    
print(pald(25))
print(pald(55))