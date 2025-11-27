import math
def numberOperation():
    try: 
        number = int(input("Number: "))
        return math.pow(number, 3)
    except:
        print("Invalid number")
    
print(numberOperation())