import collections
import heapq

def maxSlidingWindow(nums, k):
    if len(nums) <= k:
        return [max(nums)]

    h = []
    lookup = collections.defaultdict(int)
    for i in range(k):
        heapq.heappush(h, -nums[i])
        lookup[nums[i]] += 1

    res = [-h[0]]
    for j in range(k, len(nums)):
        lookup[nums[j]] += 1
        lookup[nums[j-k]] -= 1
        heapq.heappush(h, -nums[j])
        while lookup[-h[0]] == 0:
            heapq.heappop(h)
        res.append(-h[0])
    return res


nums = [1,3,-1,-4,5, 3, -6, 8, 2, 15, 7, 9, 5]
k = 4
print(maxSlidingWindow(nums, k))