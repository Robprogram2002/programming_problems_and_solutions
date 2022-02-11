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
