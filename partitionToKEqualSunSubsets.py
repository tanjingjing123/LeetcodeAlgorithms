def canPartition(nums, k):
    sum_num = sum(nums)
    if sum_num % k != 0:
        return False

    sum_of_sub = int(sum_num/k)
    used = [False] * len(nums)
    nums.sort(reverse=True)
    def helper(t, k, idx):
        if k == 0:
            return True
        if t == 0:
            return helper(sum_of_sub, k - 1, 0)
        else:
            for i in range(idx, len(nums)):
                if not used[i] and t - nums[i] >= 0:
                    used[i] = True
                    if helper(t-nums[i], k, i + 1):
                         return True
                    used[i] = False
    return True if helper(sum_of_sub, k, 0) else False


nums = [4,3,2,3,5,2,1]
k = 4
print(canPartition(nums, k))