number = int(input())
if (number % 10) % 5 == 0:
    print("Цифрата на единиците се дели на 5")
number = number // 10
if ((number % 10) % 2 == 0):
    print("Цифрата на десетиците е четно число")