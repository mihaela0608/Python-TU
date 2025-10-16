# Четвърта задача
number = int(input("number="))
valid = True
if number % 2 == 0 and number !=2:
    valid = False
if number % 3 == 0 and number !=3:
    valid = False 
if number % 5 == 0 and number !=5:
    valid = False

if valid:
    print("Числото е просто")
else:
    print("Числото не e просто")