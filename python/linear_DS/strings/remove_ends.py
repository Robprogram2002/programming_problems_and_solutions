# 1._ create a function that removes the first and last characters of a string. You're given one parameter,
# the original string.

def remove_ends(original: str) -> str:
    # using list comprehension syntax and the range function
    # return ''.join([original[k] for k in range(1, len(original) - 1)])

    # slicing the original string
    return original[1:-1]


word = "this is a beautiful day"
print(remove_ends(word))
