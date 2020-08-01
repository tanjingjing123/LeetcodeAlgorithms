import bisect


def countSmaller(nums):
    res = []
    visited = []
    for i in range(len(nums))[::-1]:
        tmp_cnt = bisect.bisect_left(visited, nums[i])
        res.append(tmp_cnt)
        visited.insert(tmp_cnt, nums[i])
    return res[::-1]

nums = [5,2,6,4,3,1,9,5]
print(countSmaller(nums))