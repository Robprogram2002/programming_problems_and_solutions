# 2._ Create a function that can transform a string into a number.

def string_to_number(string: str) -> int:
    if string[0] == '-':
        return -string_to_number(string[1:])

    result = 0
    for k in range(len(string), 0, -1):
        number = int(string[k - 1]) * (10 ** (len(string) - k))
        result += number
    return result
