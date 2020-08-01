import heapq
def isPossible(nums, k):
    nums.sort()
    sequences = dict()
    for num in nums:
        current_size, res = 1, True
        if num - 1 in sequences.keys() and sequences[num - 1]:
            current_size = heapq.heappop(sequences[num - 1])
            current_size += 1
        if current_size < k:
            if num in sequences.keys():
                heapq.heappush(sequences[num], current_size)
            else:
                sequences[num] = [current_size]
    for v in sequences.values():
        if v: return False
    return True


nums = [3,2,1,2,3,4,3,4,5,9,10,11]
k = 3
print(isPossible(nums, k))
