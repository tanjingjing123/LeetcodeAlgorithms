def reversePairs(nums):
    import bisect
    res = []
    count = 0
    for x in nums[::-1]:
        count += bisect.bisect_left(res, x)
        x = x + x
        bisect.insort(res, x)
    return count

nums = [2,4,3,5,1]
print(reversePairs(nums))