# 1._ given a list of numbers return the sum of all of them
from __future__ import annotations


def sum_numbers(data: [int]) -> int:
    # we can use list comprehension syntax (generator) and the built-in sum function
    return sum(number for number in data)


def sum_numbers_recursive(data: [int], pointer: int = 0) -> int:
    # we can use recursion to sum all the numbers in a binary operation
    if pointer + 1 == len(data):
        return data[-1]
    else:
        return data[pointer] + sum_numbers_recursive(data, pointer + 1)


# 1._ given a list of numbers return the sum of all positive ones

def sum_positives(data: [int]) -> int:
    return sum(number for number in data if number >= 0)


def sum_positives_recursive(data: [int], pointer: int = 0) -> int:
    # we can use recursion to sum all the numbers in a binary operation
    if pointer + 1 == len(data):
        return data[-1] if data[-1] > 0 else 0
    elif data[pointer] > 0:
        return data[pointer] + sum_positives_recursive(data, pointer + 1)
    else:
        return 0 + sum_positives_recursive(data, pointer + 1)


print(sum_positives_recursive([1, 2, 3, 4, 5, 6, 7, 8, -10]))
print(sum_positives_recursive([1, 2, 3, 4, -10, 5, 6, 7, 8]))
