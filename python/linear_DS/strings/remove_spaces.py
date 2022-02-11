# 3.  remove the spaces from the string, then return the resultant string.

def remove_spaces(original: str) -> str:
    return ''.join(char for char in original if char != ' ')
