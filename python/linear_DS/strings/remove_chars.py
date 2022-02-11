# 5._ Your task is to write a function that takes a string and return a new string with all vowels removed.
# improve: accept a list as argument such that it contains the characters to be removed

def remove_characters(original: str, characters: [str]) -> str:
    return ''.join(s for s in original if s.lower() not in characters)


print(remove_characters("This website is for losers LOL!", ['a', 'e', 'i', 'o', 'u']))
