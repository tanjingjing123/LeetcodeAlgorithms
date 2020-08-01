def canPartition(nums):
    s = sum(nums)
    if s % 2 != 0:
        return False
    target = s // 2
    nums.sort()
    n = len(nums)

    def backtrack(start, curr_sum):
        if curr_sum == target:
            return True
        if curr_sum > target:
            return False
        prev = '#'
        for i in range(start, n - 1):
            if nums[i] != prev:
                prev = nums[i]
                if backtrack(i + 1, curr_sum + nums[i]):
                    return True
        return False

    return backtrack(0, 0)

nums = [1, 1, 4, 6, 7, 8, 8, 9, 10]
print(canPartition(nums))