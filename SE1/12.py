inp = input()
primeSum = 0
nonPrimeSum = 0

while inp!="stop":
    number = int(inp)
    if(number < 0):
        print("Number is negative")
        inp = input()
        continue
    valid = False
    if number % 2 == 0 and number !=2:
        valid = True
    if number % 3 == 0 and number !=3:
        valid = True 
    if number % 5 == 0 and number !=5:
        valid = True
    if number % 7 == 0 and number !=7:
        valid = True

    if valid:
        nonPrimeSum+=number
    else:
        primeSum+=number
    
    inp = input()
print(f"Sum of all prime numbers: %d" %(primeSum))
print(f"Sum of all non prime numbers: %d" %(nonPrimeSum))
