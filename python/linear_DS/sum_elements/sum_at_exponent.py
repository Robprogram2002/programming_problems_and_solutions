# 2._ Write a function that calculate the sum of every number taking each at the given exponent

def sum_by_exponent(numbers: [int], n: int) -> int:
    return sum(x ** n for x in numbers)


print(sum_by_exponent([2, 3, 4, 5], 2))
print(sum_by_exponent([2, 3, 4, 5], 1))
print(sum_by_exponent([2, 3, 4], 3))
