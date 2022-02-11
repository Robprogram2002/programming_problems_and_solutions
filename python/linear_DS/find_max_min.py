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


# 3._ Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case
# insensitive. The string can contain any char.

def xo(s):
    s = s.lower()
    count_x = 0
    count_o = 0
    for char in s:
        if char == 'x':
            count_x += 1
        elif char == 'o':
            count_o += 1

    return count_x == count_o


def xo_v2(s):
    count_x = 0
    count_o = 0
    for char in s:
        if char in 'xX':
            count_x += 1
        elif char in 'oO':
            count_o += 1

    return count_x == count_o


# 4._ Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive
# integers

def sum_two_smallest_numbers(numbers):
    lowests = [numbers[0], None]
    for k in range(1, len(numbers)):
        num = numbers[k]
        if num <= lowests[0]:
            lowests[1] = lowests[0]
            lowests[0] = num
        elif lowests[1] is None or num <= lowests[1]:
            lowests[1] = num

    return sum(lowests)
