# 1._ Write a program that finds the summation of every number from 1 to num. The number will always be a positive
# integer greater than 0.

def n_sum(n: int) -> int:
    if n == 0:
        return 0
    else:
        return n + n_sum(n - 1)


print(n_sum(10))


# 2._ Given two integers a and b, which can be positive or negative, find the sum of all the integers between and
# including them and return it. If the two numbers are equal return a or b.
# Note: a and b are not ordered!

def sum_recursive(a, b):
    if a == b:
        return b
    else:
        return a + sum_recursive(a + 1, b)


def get_sum_between(a, b):
    if a <= b:
        return sum_recursive(a, b)
    else:
        return sum_recursive(b, a)
