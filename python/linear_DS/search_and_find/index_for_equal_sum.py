# 15 ._ You are going to be given an array of integers. Your job is to take that array and find an index N where the
# sum of the integers to the left of N is equal to the sum of the integers to the right of N. If there is no index
# that would make this happen, return -1.

def find_equal_sum_index(arr):
    for k in range(len(arr)):
        if sum(arr[x] for x in range(0, k)) == sum(arr[x] for x in range(k + 1, len(arr))):
            return k
    return -1
