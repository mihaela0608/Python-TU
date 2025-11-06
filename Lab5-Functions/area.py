def square(a):
    print(a*a)
def rectangle(a, b):
    print(a*b)
def triangle(a, b):
    print(a*b / 2)



def area(n):
    if(n==1):
        a = float(input("Въведете страна:"))
        square(a)
    elif(n==2):
        a = float(input("Въведете страната a:"))
        b = float(input("Въведете страната b:"))
        rectangle(a, b)
    elif(n==3):
        a = float(input("Въведете катета a:"))
        b = float(input("Въведете катета b:"))
        triangle(a, b)
   

area(1)
area(2)
area(3)