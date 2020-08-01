def checkPrerequisite(n, prerequisites, queries):
    g = [[] for _ in range(n)]
    q = [set() for _ in range(n)]
    for u, v in prerequisites:
        g[u].append(v)

    def dfs(i):
        if q[i]:
            return q[i]
        q[i].update(g[i])
        for j in g[i]:
            q[i].update(dfs(j))
        return q[i]

    for i in range(n):
        dfs(i)
    return [b in q[a] for a, b in queries]

n = 5
prerequisites = [[0,1],[1,2],[2,3],[3,4]]
queries = [[0,4],[4,0],[1,3],[3,0]]
print(checkPrerequisite(n, prerequisites, queries))