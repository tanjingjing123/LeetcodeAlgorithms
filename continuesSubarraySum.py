def checkSubarray(nums, k):
    s = 0
    d = {0: -1}
    for i in range(len(nums)):
        s = s + nums[i]
        if k != 0:
            s = s % k

        if s in d:
            if i - d[s] >= 2:
                return True
        else:
            d[s] = i
    return False

nums = [23, 2, 6, 4, 7]
k = 3
print(checkSubarray(nums, k))