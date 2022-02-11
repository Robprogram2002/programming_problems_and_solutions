# 11._ Given an array of integers, find the one that appears an odd number of times.

# simple but inefficient: word case is near O(n*n)
def find_odd_v1(seq):
    uniques = set(seq)
    for num in uniques:
        repetitions = sum(1 for k in seq if k == num)
        if repetitions % 2 == 1:
            return num


# more efficient but use more space: time O(nlogn) , space O(n)
def find_odd_v2(seq):
    numbers = [k for k in seq]
    numbers.sort()

    value = numbers[0]
    count = 1
    for k in range(1, len(numbers)):
        if numbers[k] == value:
            count += 1
        else:
            if count % 2 != 0:
                return value
            else:
                value = numbers[k]
                count += 1

    return value if count % 2 != 0 else None


# the lowest time complexity but more space consume: time is O(n) , space is O(n)

def find_odd_v3(seq):
    counts = {}
    for num in seq:  # O(n)
        if num in counts:
            counts[num] += 1
        else:
            counts[num] = 1

    for key in counts:  # O(b) where b is the number of unique elements in the sequence, so b < n
        if counts[key] % 2 != 0:
            return key

    return None  # time O(n + b) -> O(n) since b < n always
