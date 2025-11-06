def changeList(list, num):
    for i in range(0, len(list)):
        if (list[i] > num):
           list[i] = 0
    return list
print(changeList([5, 8, 17, 3, 2, 4, 16], 5))

