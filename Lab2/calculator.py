#Трета допълнителна задача
a = float(input("first number="))
b = float(input("second number="))
operator = input("operator=")

if operator == '+':
    print(f'sum= %.2f' %(a + b))
elif operator == '-':
    print(f'substraction= %.2f' %(a - b))
elif operator == '*':
    print(f'multiplication= %.2f' %(a * b))
elif operator == '/':
    if b == 0:
        print("Invalid operation!")
    else:
        print(f'division= %.2f' %(a / b))