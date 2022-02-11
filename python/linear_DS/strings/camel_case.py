# 10._ convert string to camel case
# Complete the method/function so that it converts dash/underscore delimited words into camel casing. The first word
# within the output should be capitalized only if the original word was capitalized (known as Upper Camel Case, also
# often referred to as Pascal case).

def to_camel_case(text):
    result = [''] * len(text)
    upper = False
    for i in range(len(text)):
        if text[i] == '-' or text[i] == '_':
            upper = True
        elif upper:
            result[i] = text[i].upper()
            upper = False
        else:
            result[i] = text[i]
    return ''.join(result)
