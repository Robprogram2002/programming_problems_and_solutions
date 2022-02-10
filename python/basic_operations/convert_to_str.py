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


# 2._ Create a function that can transform a string into a number.

def string_to_number(string: str) -> int:
    if string[0] == '-':
        return -string_to_number(string[1:])

    result = 0
    for k in range(len(string), 0, -1):
        number = int(string[k - 1]) * (10 ** (len(string) - k))
        result += number
    return result


# 3._ you are asked to square every digit of a number and concatenate them. For example, if we run 9119 through the
# function, 811181 will come out, because 92 is 81 and 12 is 1.
# Note: The function accepts an integer and returns an integer

def square_digits(num: int) -> int:
    # squares = [str(int(x)**2) for x in str(num)]
    # return int(''.join(squares))
    return int(''.join(str(int(x) ** 2) for x in str(num)))


# 4._ Your task is to make a function that can take any non-negative integer as an argument and return it with its
# digits in descending order. Essentially, rearrange the digits to create the highest possible number.

def descending_order(num: int) -> int:
    if num < 10:
        return num
    return int(''.join(sorted(str(num), reverse=True)))


# 5._ The examples below show you how to write function accum:

# accum("abcd") -> "A-Bb-Ccc-Dddd"
# accum("RqaEzty") -> "R-Qq-Aaa-Eeee-Zzzzz-Tttttt-Yyyyyyy"
# accum("cwAt") -> "C-Ww-Aaa-Tttt"

def accumulator(s: str) -> str:
    return '-'.join((s[k].upper() + s[k].lower() * k) for k in range(len(s)))


# 6. _ You are going to be given a word. Your job is to return the middle character of the word. If the word's length
# is odd, return the middle character. If the word's length is even, return the middle 2 characters. Examples:

# Kata.getMiddle("test") should return "es"
# Kata.getMiddle("testing") should return "t"
# Kata.getMiddle("middle") should return "dd"
# Kata.getMiddle("A") should return "A"

def get_middle(s):
    middle = (len(s) - 1) // 2
    return s[middle:middle + 2] if len(s) % 2 == 0 else s[middle]


# 7._ An isogram is a word that has no repeating letters, consecutive or non-consecutive. Implement a function that
# determines whether a string that contains only letters is an isogram. Assume the empty string is an isogram.
# Ignore letter case.

def is_isogram(string):
    # using python sets
    # return len(string) == len(set(string.lower()))

    string = string.lower()
    letters = {}

    for char in string:
        if char not in letters:
            letters[char] = 0
        else:
            return False

    return True
