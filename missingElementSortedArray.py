def missingElement(nums, k):
    if not nums:
        return k

    cur = nums[0]
    i = 1
    while i < len(nums):
        diff = nums[i] - cur - 1
        if diff == k:
            return nums[i] - 1

        elif k < diff:
            return cur + k

        else:
            k -= diff
            cur = nums[i]
        i += 1

    if k != 0:
        return cur + k

    return -1


nums = [4,7,9,10]
k = 3
print(missingElement(nums, k))