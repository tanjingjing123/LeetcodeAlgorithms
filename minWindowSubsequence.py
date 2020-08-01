import bisect
import collections
class solution:
    def minWindow(self, S, T):
        dict_s = collections.defaultdict(list)
        for i in range(len(S)):
            dict_s[S[i]].append(i)
        res = (float('inf'), -1, -1)
        for index in dict_s[T[0]]:
            end = self.dfs(index, S, T, 1, dict_s)
            if end - index < res[0]:
                res = (end - index, index, end + 1)
        return S[res[1]:res[2]]

    def dfs(self, last, S, T, i, dict_s):
        if i == len(T):
            return last
        curEntry = dict_s[T[i]]
        index = bisect.bisect_right(curEntry, last)
        if index == len(curEntry):
            return float('inf')

        return self.dfs(curEntry[index], S, T, i+1, dict_s)


S = "abcfdebddce"
T = "bde"
obj = solution()
print(obj.minWindow(S, T))