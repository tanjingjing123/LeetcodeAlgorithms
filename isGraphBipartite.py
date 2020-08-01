import collections


def isBipartite(graph):
    N, colored = len(graph), {}
    for i in range(N):
        if (i not in colored and graph[i]):
            colored[i] = 1
            queue = collections.deque([i])
            while queue:
                curr = queue.popleft()
                for nb in graph[curr]:
                    if (nb not in colored):
                        colored[nb] = 1 - colored[curr]
                        queue.append(nb)
                    elif (colored[curr] == colored[nb]):
                        return False

    return True


graph = [[1,3], [0,2], [1,3], [0,2]]
print(isBipartite(graph))