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
