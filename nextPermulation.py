def nextPermute(nums):
    def swap(i, j):
        while i < j:
            nums[i], nums[j] = nums[j], nums[i]
            i += 1
            j -= 1
        return
    n = len(nums)
    for i in range(n-2, -1, -1):
        if nums[i] < nums[i+1]:
            for j in range(len(nums) - 1, i, -1):
                if nums[j] > nums[i]:
                    nums[i], nums[j] = nums[j], nums[i]
                    swap(i+1, n-1)
                    return
    swap(0, n - 1)

nums = [8, 6, 4, 1]
print(nextPermute(nums))