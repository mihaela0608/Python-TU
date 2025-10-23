number = int(input())
numbers = [digit for digit in range(1, number+1)]
keys = numbers.copy()
numbers.reverse()
values = numbers
print(keys)
print(values)

d = {}
for i in range(0, len(keys)):
    d[keys[i]] = values[i]
print(d)