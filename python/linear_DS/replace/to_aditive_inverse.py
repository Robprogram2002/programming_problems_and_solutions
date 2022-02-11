# 4._ Given a set of numbers, return the additive inverse of each. Each positive becomes negatives, and the negatives
# become positives.

def num_to_inverse(lst: [int]) -> [int]:
    # result = [0] * len(lst)
    # for k in range(len(lst)):
    #     result[k] = -lst[k] if lst[k] != 0 else 0
    # return result
    return [-number for number in lst]
