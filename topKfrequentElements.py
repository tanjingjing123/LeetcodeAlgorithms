import collections
def topKElements(nums, k):
    list_counts = collections.Counter(nums)
    return [k for k, v in list_counts.most_common(k)]

nums = [1,1,1,2,2,3]
k = 2
print(topKElements(nums, k))
