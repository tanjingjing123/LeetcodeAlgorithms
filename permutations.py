def permute(nums):
    res = []
    def dfs(ind):
        if ind == 1:
            res.append(nums[:])
            return
        else:
            for i in range(ind):
                dfs(ind - 1)
                if i < ind - 1:
                    if ind % 2:
                        nums[0], nums[ind - 1] = nums[ind - 1], nums[0]
                    else:
                        nums[i], nums[ind - 1] = nums[ind - 1], nums[i]
    dfs(len(nums))
    return res

num = [1,2,3, 4]
print(permute(num))