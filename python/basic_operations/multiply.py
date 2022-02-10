# 1._ given two numbers return their product

def multiply_simple(n: int, m: int) -> int:
    return n * m


def multiply_recursive(n: int, m: int) -> int:
    if m == 1:
        return n
    else:
        return n + multiply_recursive(n, m - 1)


# 2._ Given a year, return the century it is in.

# The first century spans from the year 1 up to and including the year 100, the second century - from the year 101 up
# to and including the year 200, etc.

def century(year: int) -> int:
    return (year - 1) // 100 + 1


print(century(1705))  # 18
print(century(1900))  # 19
print(century(89))  # 1
print(century(356))  # 4

