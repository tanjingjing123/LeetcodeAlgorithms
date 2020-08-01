def wiggleMaxLength(nums):
    if len(nums) < 2:
        return len(nums)
    helper = []
    for i in range(1, len(nums)):
        if nums[i] > nums[i-1]:
            helper.append(1)
        elif nums[i] < nums[i-1]:
            helper.append(-1)
    result = len(helper) + 1
    for i in range(1, len(helper)):
        if helper[i] == helper[i-1]:
            result -= 1
    return result

nums = [1,17,5,10,13,15,10,5,16,8]
print(wiggleMaxLength(nums))