# 13._ sort the odds
# You will be given an array of numbers. You have to sort the odd numbers in ascending order while leaving the even
# numbers at their original positions. Examples:

# [7, 1]  =>  [1, 7]
# [5, 8, 6, 3, 4]  =>  [3, 8, 6, 5, 4]
# [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]  =>  [1, 8, 3, 6, 5, 4, 7, 2, 9, 0]

def sort_array(numbers):
    result = []
    for number in numbers:
        # append each number to the array, # if the number is even just continue
        result.append(number)
        if number % 2 != 0:  # if the number is odd, move it to its ordered position
            sort_odds(result)
    return result


# use two pointers to move the last odd number added to its ordered position doing swaps
def sort_odds(data):
    start = len(data) - 1
    end = start - 1
    while end >= 0:
        if data[end] % 2 != 0 and data[end] > data[start]:
            data[end], data[start] = data[start], data[end]
            start = end
            end = start - 1
        else:
            end -= 1
