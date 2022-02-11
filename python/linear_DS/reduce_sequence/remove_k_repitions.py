# 15._ Given a list lst and a number N, create a new list that contains each number of lst at most N times without
# reordering. For example if N = 2, and the input is [1,2,3,1,2,1,2,3], you take [1,2,3,1,2], drop the next [1,2] since
# this would lead to 1 and 2 being in the result 3 times, and then take 3, which leads to [1,2,3,1,2,3].

def delete_nth(order, max_e):
    counts = {}
    result = []

    for x in order:
        if x in counts:
            if counts[x] < max_e:
                result.append(x)
                counts[x] += 1
        else:
            counts[x] = 1
            result.append(x)
    return result
