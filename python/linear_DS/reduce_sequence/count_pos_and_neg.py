# 5._ Return an array, where the first element is the count of positives numbers and the second element is sum of
# negative numbers. 0 is neither positive nor negative.

# 6._ Given an array of integers.
# Return an array, where the first element is the count of positives numbers and the second element is sum of negative
# numbers. 0 is neither positive nor negative.
# If the input array is empty or null, return an empty array

def count_positives_sum_negatives(arr):
    if not arr or len(arr) == 0:
        return []
    count = 0
    sum = 0
    for k in range(len(arr)):
        if arr[k] > 0:
            count += 1
        else:
            sum += arr[k]
    return [count, sum]
