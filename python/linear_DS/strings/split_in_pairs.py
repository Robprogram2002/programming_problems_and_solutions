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
