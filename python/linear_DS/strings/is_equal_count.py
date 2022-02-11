# 3._ Check to see if a string has the same amount of 'x's and 'o's. The method must return a boolean and be case
# insensitive. The string can contain any char.

def xo(s):
    s = s.lower()
    count_x = 0
    count_o = 0
    for char in s:
        if char == 'x':
            count_x += 1
        elif char == 'o':
            count_o += 1

    return count_x == count_o


def xo_v2(s):
    count_x = 0
    count_o = 0
    for char in s:
        if char in 'xX':
            count_x += 1
        elif char in 'oO':
            count_o += 1

    return count_x == count_o
