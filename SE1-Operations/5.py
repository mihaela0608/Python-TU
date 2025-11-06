n = int(input())
min = 0
max = 0
for i in range(1, n+1):
    number = int(input())
    if number < min:
        min = number
    if number > max:
        max = number
print("Min: ", min)
print("Max: ", max)