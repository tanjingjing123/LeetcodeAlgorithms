import bisect

def leastSub(nums):

    piles = [0] * len(nums)

    size = 0
    for val in nums:
        index = bisect.bisect_left(piles, val, 0, size)
        piles[index] = val
        if index == size:
            size += 1

    return size


print(leastSub([2, 9, 12, 13, 4, 7, 6, 5, 10]))
