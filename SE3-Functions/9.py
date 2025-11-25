import random
def createMatrix(rows, columns):
    matrix = []
    for i in range(rows):
        row = []
        for j in range(columns):
            num = random.randint(-10, 10)
            row.append(num)
        matrix.append(row)
    
    return matrix

def printMatrix(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    for r in range(rows):
        for c in range(columns):
            print(matrix[r][c], end = " ")
        
        print()

def sumColumns(matrix):
    rows = len(matrix)
    columns = len(matrix[0])
    for c in range(columns):
        sum = 0
        for r in range(rows):
            sum+=matrix[r][c]
        print(sum, end=" ")

matrix = createMatrix(2, 4)
printMatrix(matrix)
sumColumns(matrix)