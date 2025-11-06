m = int(input())
n = int(input())
multiplication = 1
for i in range(m, n+1):
    if i % 3 == 0 and i % 4 == 0:
        multiplication*=i
if multiplication!=1:
    print("Произведението е:", multiplication)
else:
    print("Числата в този интервл не са кратни на 3 и 4")
