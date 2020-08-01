import heapq
def kSmallestPairs(nums1, nums2, k):
    res = []
    if not nums1 or not nums2 or k == 0:
        return res
    minHeap = []
    # Time O(min(n1, k))
    for i in range(min(len(nums1), k)):
        minHeap.append((nums1[i] + nums2[0], nums1[i], nums2[0], 0))
    heapq.heapify(minHeap)
    # Time O(klogk)
    while k > 0 and minHeap:
        cur = heapq.heappop(minHeap)
        res.append([cur[1], cur[2]])
        indexOfnum2 = cur[3]
        k -= 1
        if indexOfnum2 == len(nums2) - 1:
            continue
        nextCandidate = (cur[1] + nums2[indexOfnum2 + 1], \
                         cur[1], nums2[indexOfnum2 + 1], indexOfnum2 + 1)
        heapq.heappush(minHeap, nextCandidate)
    return res

nums1 = [1,2,5,7,11, 14, 15]
nums2 = [2,4,5,6,7]
k = 7
print(kSmallestPairs(nums1, nums2, k))