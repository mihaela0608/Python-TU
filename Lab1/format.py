a = int(input("a="))
b = int(input("b="))
s = "area"

print("a = " + str(a) + " b = " + str(b) + " S = " + str(a * b))
print('a = %d ; b = %d ; %s = %.2f' % (a, b, s, a * b))
print('a = {} b = {} S = {}' .format(a, b, a * b))
print(f'a = {a} b = {b} {s} = {a * b}')
