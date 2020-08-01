def fourSum(nums, target):
    nums.sort()
    di = {}
    op = []
    aim = target
    for x in range(0, len(nums) - 3):
        aim = target
        for y in range(x + 1, len(nums) - 2):
            aim = target - (nums[y] + nums[x])
            for z in range(y + 1, len(nums)):
                comp = aim - nums[z]
                if comp in di:
                    l = [nums[x], nums[y], nums[di[comp]], nums[z]]
                    if l not in op:
                        op.append(l)
                    di[nums[z]] = z
                else:
                    di[nums[z]] = z
            di.clear()

    return op


nums = [4,-2,3,2,0,2,-4,1,5,0]
target = 1
print(fourSum(nums, target))