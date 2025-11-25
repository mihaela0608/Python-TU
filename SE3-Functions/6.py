def values(*args):
    minValue = min(args)
    maxValue = max(args)
    averageValue = sum(args) // len(args)
    result = [averageValue, maxValue, minValue]
    print(result)

values(7, 8, 14, 5)