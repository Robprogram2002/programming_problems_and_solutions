# 1._ Write a program that finds the summation of every number from 1 to num. The number will always be a positive
# integer greater than 0.

def n_sum(n: int) -> int:
    if n == 0:
        return 0
    else:
        return n + n_sum(n - 1)


print(n_sum(10))
