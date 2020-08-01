import heapq
import collections

def maxSliding(nums, k):
    if len(nums) <= k:
        return [max(nums)]

    heap = []
    lookup = collections.defaultdict(int)
    for i in range(k):
        heapq.heappush(heap, -nums[i])
        lookup[nums[i]] += 1
    res = [-heap[0]]

    for j in range(k, len(nums)):
        lookup[nums[j-k]] -= 1
        lookup[nums[j]] += 1
        heapq.heappush(heap, -nums[j])
        while lookup[-heap[0]] == 0:
            heapq.heappop(heap)
        res.append(-heap[0])
    return res

nums = [1,3,-1,-3,5,3,2,6,4,-2,7,5]
k = 5
print(maxSliding(nums, k))
