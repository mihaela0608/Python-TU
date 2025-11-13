ourTup = tuple(input("Word:"))
step = int(input("Step:"))
withStep = list()
for i in range(0, len(ourTup), step):
    withStep.append(ourTup[i])
finalTup = tuple(withStep)
print(finalTup)