# 1._ create a function that removes the first and last characters of a string. You're given one parameter,
# the original string.

def remove_ends(original: str) -> str:
    # using list comprehension syntax and the range function
    # return ''.join([original[k] for k in range(1, len(original) - 1)])

    # slicing the original string
    return original[1:-1]


word = "this is a beautiful day"
print(remove_ends(word))


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


print(reverse_string(word))


# 3.  remove the spaces from the string, then return the resultant string.

def remove_spaces(original: str) -> str:
    return ''.join(char for char in original if char != ' ')


print(remove_spaces(word))


# 4. Reversed words. Complete the solution so that it reverses all of the words within the string passed in.
# Example :
# "The greatest victory is that which requires no battle" --> "battle no requires which that is victory greatest The"

def reverse_words(original: str) -> str:
    word_list = original.split(' ')
    return ' '.join(reversed(word_list))

    # reverse elements using our own function

    # _reverse_recursive(word_list, 0, len(word_list))
    # return ' '.join(word_list)


print(reverse_words("The greatest victory is that which requires no battle"))


# 5._ Your task is to write a function that takes a string and return a new string with all vowels removed.
# improve: accept a list as argument such that it contains the characters to be removed

def remove_characters(original: str, characters: [str]) -> str:
    return ''.join(s for s in original if s.lower() not in characters)


print(remove_characters("This website is for losers LOL!", ['a', 'e', 'i', 'o', 'u']))


# 6._ Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.

def find_short(s):
    words = s.split(' ')
    result = len(words[0])
    for k in words:
        if len(k) < result:
            result = len(k)
    return result
