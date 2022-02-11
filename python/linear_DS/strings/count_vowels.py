# 8. Return the number (count) of vowels in the given string. The input string will only consist of lower case letters
# and/or spaces.

def get_vowels_count(sentence):
    vowels = 'aeiou'
    return sum(1 for char in sentence if char in vowels)


# 9. Return the number of each vowels in the given string
def get_each_vowel_count(sentence: str) -> {str: int}:
    result = {
        'a': 0,
        'e': 0,
        'i': 0,
        'o': 0,
        'u': 0,
    }
    for char in sentence:
        if char in result:
            result[char] += 1
    return result


print(get_vowels_count('today is a beautiful day'))
print(get_each_vowel_count('today is a beautiful day'))
