def threeSumCloset(nums, target):
    n = len(nums)
    nums.sort()
    res = sum(nums[:3])
    for i in range(n-2):
        j = i + 1
        k = n - 1
        while j < k:
            tem = nums[i] + nums[j] + nums[k]
            if abs(target - tem) < abs(target - res):
                res = tem
            if tem < target:
                j += 1
            else:
                k -= 1

    return res

nums = [-1, 2, 1, -4]
print(threeSumCloset(nums, target=1))