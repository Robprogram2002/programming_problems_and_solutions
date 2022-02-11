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
