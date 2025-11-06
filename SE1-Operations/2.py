sum = 0
count = 0
for i in range (7, 71):
    if i % 3 == 0:
        sum+=i
        count+=1
print("Средноаритметично:", sum/count)