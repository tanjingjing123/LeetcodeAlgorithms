import collections
def subarraySum(nums, k):
    count = 0
    hm = collections.defaultdict(int)
    hm[0] = 1
    sum = 0
    for num in nums:
        sum += num
        if sum - k in hm:
            count += hm[sum-k]
        hm[sum] += 1
    return count

nums = [2, 4, 3, 1, 2, 4, 5, 1]
k = 6
print(subarraySum(nums, k))