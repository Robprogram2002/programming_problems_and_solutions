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
