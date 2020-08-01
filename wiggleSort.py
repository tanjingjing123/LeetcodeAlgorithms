def wiggleSort(nums):
    i = 0
    while (i < len(nums)):
        j = i
        while (j < i + 2 and j < len(nums) - 1):
            if j % 2 == 0:
                if nums[j] > nums[j+1]:
                    nums[j+1], nums[j] = nums[j], nums[j+1]

            else:
                if nums[j] < nums[j+1]:
                    nums[j+1], nums[j] = nums[j], nums[j+1]
            j += 1
        i = i + 2

