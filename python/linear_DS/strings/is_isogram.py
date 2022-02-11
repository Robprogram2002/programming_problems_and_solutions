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
