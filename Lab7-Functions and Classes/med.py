numbers = input().split(" ")
if len(numbers) % 2 != 0:
    index = len(numbers) // 2
    print(index + 1)
else:
    index = len(numbers) // 2
    print((int(numbers[index-1]) + int(numbers[index])) / 2)