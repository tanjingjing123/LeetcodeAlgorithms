import collections
import heapq
def findTheCity(n, edges, distanceThreshold):
    adj = collections.defaultdict(dict)
    for a,b,c in edges:
        adj[a][b] = adj[b][a] = c
    def bfs(s, distanceThreshold):
        visited = [False] * n
        dist = [float('inf')] * n
        frontier = [(0, s)]
        visited[s] = True
        dist[s] = 0
        while not all(visited) and frontier:
            d, s = heapq.heappop(frontier)
            if d > distanceThreshold: break
            dist[s] = d
            visited[s] = True
            for t in adj[s]:
                if not visited[t]:
                    heapq.heappush(frontier, (d + adj[s][t], t))
        return len([d for d in dist if d <= distanceThreshold])
    res = 0
    count = n
    for i in range(n):
        c = bfs(i, distanceThreshold)
        if c <= count:
            res = max(res, i)
            count = c
    return res

n = 5
edges = [[0,1,2],[0,4,3],[1,2,3],[1,4,2],[2,3,1],[3,4,1]]
distanceThreshold = 4
print(findTheCity(n, edges, distanceThreshold))
