# 4._ Create a function that returns the sum of the two lowest positive numbers given an array of minimum 4 positive
# integers

def sum_two_smallest_numbers(numbers):
    lowests = [numbers[0], None]
    for k in range(1, len(numbers)):
        num = numbers[k]
        if num <= lowests[0]:
            lowests[1] = lowests[0]
            lowests[0] = num
        elif lowests[1] is None or num <= lowests[1]:
            lowests[1] = num

    return sum(lowests)
