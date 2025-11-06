def calculator(a, b, operation):
    if(operation == "+"):
        return a + b
    elif(operation == "-"):
        return a - b
    elif(operation == "*"):
        return a * b
    elif(operation == "/"):
        return a / b
    elif(operation == "**"):
        return a ** b
    elif(operation == "%"):
        return a % b
    else:
        return "Invalid operation"
    
a = float(input("a="))
operation = input("Operation: ")
b = float(input("b="))

print(calculator(a, b, operation))