numbers = list(map(int, input().split(" ")))
numbers = [(lambda x: -x if x < 0 else x)(x) for x in numbers]


print(numbers)
