def maxProduct(nums):
    if len(nums) == 1:
        return nums[0]

    cur_pr_min = cur_pr_max = res = nums[0]

    for n in nums[1:]:
        cur_pr_max, cur_pr_min = max(n, cur_pr_max * n, cur_pr_min * n), min(n, cur_pr_max * n, cur_pr_min * n)

        if cur_pr_max > res:
            res = cur_pr_max

    return res

nums = [-2, 3, -4]
print(maxProduct(nums))