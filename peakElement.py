def findPeakElement(nums):
    def helper(l, r):
        if l == r:
            return l
        if l + 1 == r:
            if nums[l] > nums[r]:
                return l
            else:
                return r
        m = (r + l) // 2
        if nums[m - 1] < nums[m] > nums[m + 1]:
            return m
        if nums[m - 1] < nums[m] < nums[m + 1]:
            return helper(m + 1, r)
        else:
            return helper(l, m - 1)
    ln = len(nums)
    if ln == 0:
        return None
    return helper(0, ln - 1)


nums = [1,2,4,3,5,6,8,2,3]
print(findPeakElement(nums))