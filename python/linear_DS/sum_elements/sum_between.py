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
