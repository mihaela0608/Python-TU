numbers = list(input().split(" "))
unique = list(set(numbers))
unique.sort()
print(unique)
counter = list()
moreThan1 = list()

for i in numbers:
    if i in counter:
        moreThan1.append(i)
    else:
        counter.append(i)
        
moreThan1.sort()
print(moreThan1)

    
