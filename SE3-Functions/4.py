def toBinary(number):
    result = ""
    while number > 0:
        result+=str(number % 2)
        number = number // 2
    
    print(result[::-1])

toBinary(10)

        