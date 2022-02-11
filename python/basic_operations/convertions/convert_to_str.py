# 1. create a function that can transform a number into a string.

def convert_to_str(number: int) -> str:
    if number < 0:
        return '-' + convert_to_str(-number)

    stack = []
    while number > 0:
        stack.append(str(number % 10))
        number = number // 10
    # return ''.join([stack[k - 1] for k in range(len(stack), 0, -1)])
    return ''.join(stack[::-1])

print(convert_to_str(2314))
print(convert_to_str(-2324))

