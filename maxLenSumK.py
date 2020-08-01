def maxSubArrayLen(nums, k):
    i, sm, dc, length = 0, 0, {0: -1}, float('-inf')
    while i < len(nums):
        sm += nums[i]
        if sm not in dc:
            dc[sm] = i
        if (sm - k) in dc:
            length = max(length, i - dc[sm - k])
        i += 1
    return length if length != float('-inf') else 0

nums = [3, 2, -4, 3, -2, 3, 2, -3, 5, 2, -2, 3]
k = 9
print(maxSubArrayLen(nums, k))

