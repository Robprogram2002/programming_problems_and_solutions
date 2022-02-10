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


# 2._ Write a function that calculate the sum of every number taking each at the given exponent

def sum_by_exponent(numbers: [int], n: int) -> int:
    return sum(x ** n for x in numbers)


print(sum_by_exponent([2, 3, 4, 5], 2))
print(sum_by_exponent([2, 3, 4, 5], 1))
print(sum_by_exponent([2, 3, 4], 3))


# 3._ Given a random non-negative number, you have to return the digits of this number within an array in reverse order.

def digitize_reverse(n):
    if n == 0:
        return [0]

    result = []
    while n > 0:
        result.append(n % 10)
        n = n // 10

    return result


def digitize(n: int) -> [int]:
    if n == 0:
        return [0]

    result = []
    while n > 0:
        result.append(n % 10)
        n = n // 10

    return result[::-1]


print(digitize(24890))
print(digitize_reverse(24890))


# 4._ Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives
# become positives.

def num_to_inverse(lst: [int]) -> [int]:
    # result = [0] * len(lst)
    # for k in range(len(lst)):
    #     result[k] = -lst[k] if lst[k] != 0 else 0
    # return result
    return [-number for number in lst]


# 5._ Return an array, where the first element is the count of positives numbers and the second element is sum of
# negative numbers. 0 is neither positive nor negative.


# 6._ Given an array of integers.
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative
# numbers. 0 is neither positive nor negative.
# If the input array is empty or null, return an empty array

def count_positives_sum_negatives(arr):
    if not arr or len(arr) == 0:
        return []
    count = 0
    sum = 0
    for k in range(len(arr)):
        if arr[k] > 0:
            count += 1
        else:
            sum += arr[k]
    return [count, sum]


# 7. write a function that returns the average of a given list of numbers and give the option to return the result
# to the nearest low integer

def average(numbers: [int | float], floor=False) -> int | float:
    numbers_sum = sum(numbers)
    return numbers_sum // len(numbers) if floor else numbers_sum / len(numbers)


print(average([2, 3, 4, 5, 6, 7, 7]))
print(average([2, 3, 4, 5, 6, 7, 7], floor=True))


# 8. Return the number (count) of vowels in the given string. The input string will only consist of lower case letters
# and/or spaces.

def get_vowels_count(sentence):
    vowels = 'aeiou'
    return sum(1 for char in sentence if char in vowels)


# 9. Return the number of each vowels in the given string
def get_each_vowel_count(sentence: str) -> {str: int}:
    result = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0,
    }
    for char in sentence:
        if char in result:
            result[char] += 1
    return result


print(get_vowels_count('today is a beautiful day'))
print(get_each_vowel_count('today is a beautiful day'))
