def findDuplicate(nums):
    t = 0
    r = 0
    while t == 0 or t != r:
        t = nums[t]
        r = nums[r]
        r = nums[r]

    meet = t
    start = 0

    while meet != start:
        meet = nums[meet]
        start = nums[start]

    return start

nums = [4,6,7,2,8,3,2,5,1]
print(findDuplicate(nums))

