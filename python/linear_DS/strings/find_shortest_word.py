# 6._ Simple, given a string of words, return the length of the shortest word(s).
# String will never be empty and you do not need to account for different data types.

def find_short(s):
    words = s.split(' ')
    result = len(words[0])
    for k in words:
        if len(k) < result:
            result = len(k)
    return result
