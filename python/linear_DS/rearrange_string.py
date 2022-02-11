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


# 7._ Take 2 strings s1 and s2 including only letters from ato z. Return a new sorted string, the longest possible,
# containing distinct letters - each taken only once - coming from s1 or s2. Example:

# a = "xyaabbbccccdefww"
# b = "xxxxyyyyabklmopq"
# longest(a, b) -> "abcdefklmopqwxy"

def longest(a1, a2):
    return ''.join(sorted(set(a1).union(set(a2))))


# 8._ Write a function that takes in a string of one or more words, and returns the same string, but with all five or
# more letter words reversed (Just like the name of this Kata). Strings passed in will consist of only letters and
# spaces.

def spin_words(sentence):
    # using pythonian syntax
    # return " ".join([x[::-1] if len(x) >= 5 else x for x in sentence.split(" ")])
    words = sentence.split(' ')
    for k in range(len(words)):
        if len(words[k]) >= 5:
            words[k] = words[k][::-1]

    return ' '.join(words)


# 9._ given a string, replace every letter with its position in the alphabet.
# If anything in the text isn't a letter, ignore it and don't return it. Example :
# alphabet_position("The sunset sets at twelve o' clock.")
# Should return "20 8 5 19 21 14 19 5 20 19 5 20 19 1 20 20 23 5 12 22 5 15 3 12 15 3 11" ( as a string )

def alphabet_position(text):
    return ' '.join(str(ord(char) - ord('A') + 1) for char in text.upper() if char.isalpha())


# 10._ convert string to camel case
# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word
# within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also
# often referred to as Pascal case).

def to_camel_case(text):
    result = [''] * len(text)
    upper = False
    for i in range(len(text)):
        if text[i] == '-' or text[i] == '_':
            upper = True
        elif upper:
            result[i] = text[i].upper()
            upper = False
        else:
            result[i] = text[i]
    return ''.join(result)


# 11._ A pangram is a sentence that contains every single letter of the alphabet at least once. (case is irrelevant)
# Given a string, detect whether or not it is a pangram. Return True if it is, False if not. Ignore numbers and
# punctuation.

def is_pangram(s):
    characters = set()
    for char in s.lower():
        if char.isalpha() and char not in characters:
            characters.add(char)
    print(characters)
    return len(characters) == 26


def is_pangram_v2(s):
    return len(set([char for char in s.lower() if char.isalpha()])) == 26


# 12._ Find the missing letter
# Write a method that takes an array of consecutive (increasing) letters as input and that returns the missing letter
# in the array. You will always get an valid array. And it will be always exactly one letter be missing. The length of
# the array will always be at least 2. The array will always contain letters in only one case.

# Examples:
# ["a","b","c","d","f"] -> "e"
# ["O","Q","R","S"] -> "P"

def get_char_num(s, m):
    return ord(s) - ord(m)


def find_missing_letter(chars):
    upper = chars[0].isupper()
    first = ord(chars[0].upper())
    result = None
    for k in range(1, len(chars)):
        if k != ord(chars[k].upper()) - first:
            result = chr(k + first)
            break
    return result if upper else result.lower()


# 13._ sort the odds
# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even
# numbers at their original positions. Examples:

# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

def sort_array(numbers):
    result = []
    for number in numbers:
        # append each number to the array, # if the number is even just continue
        result.append(number)
        if number % 2 != 0:  # if the number is odd, move it to its ordered position
            sort_odds(result)
    return result


# use two pointers to move the last odd number added to its ordered position doing swaps
def sort_odds(data):
    start = len(data) - 1
    end = start - 1
    while end >= 0:
        if data[end] % 2 != 0 and data[end] > data[start]:
            data[end], data[start] = data[start], data[end]
            start = end
            end = start - 1
        else:
            end -= 1


# 14._ Create a function  so that it splits the string into pairs of two characters. If the string contains an odd
# number of characters then it should replace the missing second character of the final pair with an underscore ('_').
# Examples:
# solution('abc') # should return ['ab', 'c_']
# solution('abcdef') # should return ['ab', 'cd', 'ef']

def str_to_pairs(s):
    if len(s) % 2 != 0:
        s += '_'

    return [s[k] + s[k + 1] for k in range(0, len(s), 2)]


# without modifying the original string

def str_to_pairs_v2(s):
    if len(s) % 2 == 0:
        return [s[k] + s[k + 1] for k in range(0, len(s), 2)]
    else:
        return [s[k] + s[k + 1] for k in range(0, len(s) - 1, 2)]


# 15._ Given a list lst and a number N, create a new list that contains each number of lst at most N times without
# reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since
# this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].

def delete_nth(order, max_e):
    counts = {}
    result = []

    for x in order:
        if x in counts:
            if counts[x] < max_e:
                result.append(x)
                counts[x] += 1
        else:
            counts[x] = 1
            result.append(x)
    return result
