import random

size = int(input("Size: "))
matrix = []
for i in range(size):
    row = []
    for k in range(size):
        number = random.randint(-10, 10)
        row.append(number)
    matrix.append(row)

for i in range(size):
    for k in range(size):
        print(matrix[i][k], end = " ")
    print()