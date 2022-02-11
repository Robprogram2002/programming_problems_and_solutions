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
