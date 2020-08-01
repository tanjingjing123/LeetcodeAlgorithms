import treeNode
class solution:
    def recur(self, n):
        if self.cache[n]  != -1:
            return self.cache[n]

        self.cache[n] = 0
        for i in range(n):
            left = self.recur(i)
            right = self.recur(n - i - 1)
            self.cache[n] += left * right
        return self.cache[n]

    def numTrees(self, n):
        self.cache = [-1] * 10000
        self.cache[0] = 1
        self.cache[1] = 1
        return self.recur(n)

obj = solution()
n = 4
print(obj.numTrees(n))