import random

mylst_15 = []
for i in range(15):
    num = random.randint(-1000, -1)
    mylst_15.append(num)

biggest = mylst_15[0]
for num in mylst_15:
    if num > biggest:
        biggest = num

sum_list = 0
for num in mylst_15:
    sum_list += num

mylst_dev3 = []
for num in mylst_15:
    if num % 3 == 0:
        mylst_dev3.append(num)

mylst_dev3.sort()

i = 1
while i < len(mylst_dev3):
    mylst_dev3.pop(i)
    i += 1
