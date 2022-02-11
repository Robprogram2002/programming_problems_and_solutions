# 7. write a function that returns the average of a given list of numbers and give the option to return the result
# to the nearest low integer
from __future__ import annotations


def average(numbers: [int | float], floor=False) -> int | float:
    numbers_sum = sum(numbers)
    return numbers_sum // len(numbers) if floor else numbers_sum / len(numbers)


print(average([2, 3, 4, 5, 6, 7, 7]))
print(average([2, 3, 4, 5, 6, 7, 7], floor=True))
