def checkPerfectNum(number):
    half = number // 2
    sum = 0
    for i in range(1, number):
        if(number%i == 0):
            sum+=i
    if(sum == number):
        return True
    else:
        return False


numbers = [1, 6, 18, 28]
for num in numbers:
    if(checkPerfectNum(num)):
        print(num)