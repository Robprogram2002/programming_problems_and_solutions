# 14 ._ Write a function, persistence, that takes in a positive parameter num and returns its multiplicative persistence,
# which is the number of times you must multiply the digits in num until you reach a single digit. Example

# 39 --> 3 (because 3*9 = 27, 2*7 = 14, 1*4 = 4 and 4 has only one digit)
# 999 --> 4 (because 9*9*9 = 729, 7*2*9 = 126, 1*2*6 = 12, and finally 1*2 = 2)

def persistence(n, count=0):
    if n < 10:
        return count

    digits = [int(k) for k in str(n)]
    result = digits[0]
    for k in range(1, len(digits)):
        result = result * digits[k]
    return persistence(result, count + 1)
