m = int(input("Start: "))
n = int(input("End: "))
numbers = list(i for i in range(m, n + 1) if ((i % 3 == 0 and i % 4 != 0) or (i % 3 != 0 and i % 4 == 0)))
print(numbers)
