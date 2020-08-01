from collections import defaultdict


class Solution:
    def criticalConnections(self, n, connections):
        self.g = defaultdict(list)
        for i in connections:
            self.g[i[0]].append(i[1])
            self.g[i[1]].append(i[0])
        self.ids = [0] * n
        self.visited = [False] * n
        self.id = 0
        self.bridges = []
        self.low = [0] * n
        for i in range(n):
            if (self.visited[i] == False):
                self.dfs(i, -1)
        return (self.bridges)

    def dfs(self, at, parent):
        self.visited[at] = True
        self.ids[at] = self.low[at] = self.id
        self.id += 1
        for v in self.g[at]:
            if (v == parent):
                continue
            if (not self.visited[v]):
                self.dfs(v, at)
                self.low[at] = min(self.low[at], self.low[v])
                if (self.ids[at] < self.low[v]):
                    self.bridges.append((at, v))
            else:
                self.low[at] = min(self.low[at], self.low[v])
obj = Solution()
n = 5
connections = [[0,1],[0,2],[2,1],[0,3],[3,4]]
print(obj.criticalConnections(n, connections))