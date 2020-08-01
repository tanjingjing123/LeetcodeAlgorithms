def containsNearByDuplicate(nums, k, t):
    if t < 0: return False
    d = {}
    for i, (n, b) in enumerate(zip(nums, map(lambda x: x // (t + 1), nums))):
        if b in d or min(n - d.get(b - 1, float('-inf')), d.get(b + 1, float('inf')) - n) <= t:
            return True
        d[b] = n
        if i >= k: del d[nums[i - k] // (t + 1)]
    return False
nums = [1,5,9,1,5,9]
k = 2
t = 3
print(containsNearByDuplicate(nums, k, t))