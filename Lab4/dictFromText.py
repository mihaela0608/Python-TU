txt = list(input("Text: "))
counter = {}
for i in txt:
    if i in counter:
        counter[i] = counter[i] + 1
    else:
        counter[i] = 1
for i in counter.keys():
    print(f"%s:%d" %(i, counter[i]), end = " ")
