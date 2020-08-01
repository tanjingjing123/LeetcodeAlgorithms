def search(nums, target):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] == target:
            return mid
        if nums[start] == target:
            return start
        if nums[end] == target:
            return end

        if nums[mid] < nums[end]:
            if target > nums[mid] and target < nums[end]:
                start = mid + 1
            else:
                end = mid - 1
        else:
            if target < nums[mid] and target > nums[start]:
                end = mid - 1
            else:
                start = mid + 1
    return -1

nums = [8,9,10,11,16,18,20,3,4,6,7]
print(search(nums, target=10))
