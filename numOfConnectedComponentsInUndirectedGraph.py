class solution:
    def countComponents(self, n, edges):
        def getParent(i):
            if parent[i] != i:
                parent[i] = getParent(parent[i])
            return parent[i]

        def unionParent(a, b):
            a = getParent(a)
            b = getParent(b)
            if a > b:
                parent[b] = a
                self.ans -= 1
            elif a < b:
                parent[a] = b
                self.ans -= 1
            else:
                print('cycle')

        parent = [i for i in range(n)]
        self.ans = n
        for u, v in edges:
            unionParent(u, v)
        return self.ans
obj = solution()
n = 5
edges = [[0, 1], [1, 2], [3, 4]]
print(obj.countComponents(n, edges))
