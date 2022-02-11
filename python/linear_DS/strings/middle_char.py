# 6. _ You are going to be given a word. Your job is to return the middle character of the word. If the word's length
# is odd, return the middle character. If the word's length is even, return the middle 2 characters. Examples:

# Kata.getMiddle("test") should return "es"
# Kata.getMiddle("testing") should return "t"
# Kata.getMiddle("middle") should return "dd"
# Kata.getMiddle("A") should return "A"

def get_middle(s):
    middle = (len(s) - 1) // 2
    return s[middle:middle + 2] if len(s) % 2 == 0 else s[middle]
