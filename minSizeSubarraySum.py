import math
import bisect


def findMinSum(s, nums):
    if not nums:
        return 0
    nums = [0] + nums
    record = [0]
    res = math.inf
    for i in range(1, len(nums)):
        nums[i] += nums[i-1]
        record.append(nums[i])
        if nums[i] - s >= 0:
            idx = bisect.bisect_right(record, nums[i] - s)
            res = min(res, (i - idx + 1))
    return res if res != math.inf else 0

s = 7
nums = [2,3,1,2,4,3]
print(findMinSum(s, nums))