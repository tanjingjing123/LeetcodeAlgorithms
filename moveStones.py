import collections
class solution:
    def moveStones(self, stones):
        graph = collections.defaultdict(list)
        for i in range(len(stones)):
            for j in range(i):
                if stones[i][0] == stones[j][0] or stones[i][1] == stones[j][1]:
                    graph[i].append(j)
                    graph[j].append(i)
        visited = set()
        self.count = 0
        def dfs(graph, v):
            visited.add(v)
            for i in graph[v]:
                if i not in visited:
                    self.count += 1
                    dfs(graph, i)
        for i in range(len(stones)):
            if i not in visited:
                dfs(graph, i)
        return self.count


mywork = solution()
stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]]
print(mywork.moveStones(stones))