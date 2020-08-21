def largestSum(nums):
    maxSum = 0
    curSum = 0
    for num in nums:
        curSum += num
        if curSum >= maxSum:
            maxSum = curSum
        if curSum < 0:
            curSum = 0
    return maxSum

nums = [2, -8, 3, -2, 4, -10, 3]
print(largestSum(nums))