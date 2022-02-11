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
