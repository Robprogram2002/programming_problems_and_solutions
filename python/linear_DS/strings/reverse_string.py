# 2. given a string return a new one with the characters in reversed order

def reverse_string(original: str) -> str:
    # using python slice capabilities
    # return original[::-1]

    # using recursion and conversion between list and string
    result = list(original)
    _reverse_recursive(result, 0, len(result))
    return ''.join(result)


def _reverse_recursive(data: [], start: int, end: int) -> []:
    if start < end:
        data[start], data[end - 1] = data[end - 1], data[start]
        _reverse_recursive(data, start + 1, end - 1)
