def nok(number1, number2):
    smaller = 0
    bigger = 0
    if(number1 > number2):
        smaller = number2
        bigger = number1
    else:
        smaller = number1
        bigger = number2

    result = 1
    for i in range(2, bigger):
        while bigger % i == 0:
            
