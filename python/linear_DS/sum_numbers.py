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


# 10._ Create a function so that it returns the sum of all the multiples of 3 or 5 below the number passed in.
# Additionally, if the number is negative, return 0

def solution(number):
    return sum(x for x in range(number) if x % 3 == 0 or x % 5 == 0)


# 11._ Given an array of integers, find the one that appears an odd number of times.

# simple but inefficient: word case is near O(n*n)
def find_odd_v1(seq):
    uniques = set(seq)
    for num in uniques:
        repetitions = sum(1 for k in seq if k == num)
        if repetitions % 2 == 1:
            return num


# more efficient but use more space: time O(nlogn) , space O(n)
def find_odd_v2(seq):
    numbers = [k for k in seq]
    numbers.sort()

    value = numbers[0]
    count = 1
    for k in range(1, len(numbers)):
        if numbers[k] == value:
            count += 1
        else:
            if count % 2 != 0:
                return value
            else:
                value = numbers[k]
                count += 1

    return value if count % 2 != 0 else None


# the lowest time complexity but more space consume: time is O(n) , space is O(n)

def find_odd_v3(seq):
    counts = {}
    for num in seq:  # O(n)
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for key in counts:  # O(b) where b is the number of unique elements in the sequence, so b < n
        if counts[key] % 2 != 0:
            return key

    return None  # time O(n + b) -> O(n) since b < n always


# 12 .Digital root is the recursive sum of all the digits in a number.
# Given n, take the sum of the digits of n. If that value has more than one digit, continue reducing in this way until
# a single-digit number is produced. The input will be a non-negative integer.

def digital_root(n):
    digits = []
    while n > 0:
        digits.append(n % 10)
        n = n // 10
    value = sum(digits)
    return value if value < 10 else digital_root(value)


# 13._ Your goal in this kata is to implement a difference function, which subtracts one list from another and returns
# the result. It should remove all values from list a, which are present in list b keeping their order.

def array_diff(a, b):
    return [x for x in a if x not in b]


# 14 ._ Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
# which is the number of times you must multiply the digits in num until you reach a single digit. Example

# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)

def persistence(n, count=0):
    if n < 10:
        return count

    digits = [int(k) for k in str(n)]
    result = digits[0]
    for k in range(1, len(digits)):
        result = result * digits[k]
    return persistence(result, count + 1)


print(ord('b') - ord('a'))


# 15 ._ You are going to be given an array of integers. Your job is to take that array and find an index N where the
# sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index
# that would make this happen, return -1.

def find_even_index(arr):
    for k in range(len(arr)):
        if sum(arr[x] for x in range(0, k)) == sum(arr[x] for x in range(k + 1, len(arr))):
            return k
    return -1


# 16._ A Narcissistic Number is a positive number which is the sum of its own digits, each raised to the power of the
# number of digits in a given base. Your code must return true or false depending upon whether the given number is a
# Narcissistic number in base 10.

def get_digits(n):
    if n < 10:
        return [n]
    digits = []
    while n > 0:
        digits.append(n % 10)
        n = n // 10
    return digits


def narcissistic(value):
    digits = get_digits(value)
    n = len(digits)
    return value == sum(x ** n for x in digits)


something = {}
