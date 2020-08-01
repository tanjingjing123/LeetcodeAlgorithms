import collections
from heapq import heappush, heappop


def networkDelayTime(times, N, K):
    graph = {node: [] for node in range(1, N + 1)}
    for u, v, w in times:
        graph[u].append([v, w])
    pq = [(0, K)]
    seen = set()
    while pq:
        weight, curr = heappop(pq)
        seen.add(curr)
        for neighbor, neighbor_weight in graph[curr]:
            if neighbor not in seen:
                heappush(pq, (weight + neighbor_weight, neighbor))
        if len(seen) == N:
            return weight

    return -1

times = [[2,1,1],[2,3,1],[3,4,1]]
N = 4
K = 2
print(networkDelayTime(times, N, K))