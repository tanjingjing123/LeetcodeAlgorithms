def search(nums, target):
    start, end = 0, len(nums) - 1
    while start <= end:
        mid = (start + end) // 2
        if nums[mid] < target:
            start = mid + 1
        elif nums[mid] > target:
            end = mid - 1
        else:
            start = end = mid
            while start >= 0 and nums[start] == target:
                start -= 1
            while end < len(nums) and nums[end] == target:
                end += 1
            return [start + 1, end - 1]
    return [-1, -1]


nums = [1, 2, 2, 4, 6, 6, 7, 9, 12, 12, 13, 15, 17, 18, 18, 18, 20, 21, 21, 22]
target = 18
print(search(nums, target))