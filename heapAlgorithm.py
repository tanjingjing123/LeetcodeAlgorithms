import collections
def permute(nums):
    if not nums:
        return []

    counter = collections.Counter(nums)
    result = []
    tmpList = []
    def dfs(curUsed):
        if curUsed == len(nums):
            result.append(tmpList[:])
        for v in counter:
            if counter[v] > 0:
                tmpList.append(v)
                counter[v] -= 1
                dfs(curUsed + 1)
                tmpList.pop()
                counter[v] += 1
    dfs(0)
    return result


nums = [1, 1, 1, 3, 3]
print(permute(nums))