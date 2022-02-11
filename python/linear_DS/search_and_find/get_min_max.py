# 1. Given an array of integers your solution should find the smallest integer.
# 2. Given an array of integers your solution should find the greatest integer.

from typing import Union

num = Union[int, float]


def smallest(data: [num]) -> num:
    value = data[0]
    for k in range(1, len(data)):
        if data[k] < value:
            value = data[k]
    return value


def greatest(data: [num]) -> num:
    value = data[0]
    for k in range(1, len(data)):
        if data[k] > value:
            value = data[k]
    return value


def min_max(data: [num]) -> (num, num):
    min_val = 0
    max_val = 0
    for k in range(len(data)):
        if data[k] < min_val:
            min_val = data[k]
        elif data[k] > max_val:
            max_val = data[k]
    return min_val, max_val


print(smallest([2, 123, 235, 21, .23, -15, 1, 0, -20]))
print(greatest([2, 123, 235, 21, .23, -15, 1, 0, -20]))
print(min_max([2, 123, 235, 21, .23, -15, 1, 0, -20]))
