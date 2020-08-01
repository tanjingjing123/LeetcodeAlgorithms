def findMinHeightTrees(n, edges):
    if n == 1:
        return [0]

    graph = [[] for _ in range(n)]
    degree = [0] * n
    for a, b in edges:
        graph[a].append(b)
        graph[b].append(a)
        degree[a] += 1
        degree[b] += 1

    cur = [i for i in range(n) if degree[i] == 1]
    while cur:
        nxt = []
        for node in cur:
            degree[node] -= 1
            for _node in graph[node]:
                degree[_node] -= 1
                if degree[_node] == 1:
                    nxt.append(_node)

        if not nxt:
            return cur
        cur = nxt


n = 7
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4], [5, 6]]
print(findMinHeightTrees(n, edges))