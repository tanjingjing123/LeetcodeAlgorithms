from collections import defaultdict
import heapq
def numBusesToDestination(routes, S, T):
    if S == T:
        return 0
    queue = []
    visited = {}

    graph = defaultdict(list)
    for i in range(len(routes)):
        line = routes[i]
        if S in line:
            heapq.heappush(queue, (1, S, i))
            visited[(S, i)] = 1

        for j in range(len(line)):
            if j < (len(line) - 1):
                graph[line[j]].append((line[j+1], i))
            else:
                graph[line[j]].append((line[0], i))


    while queue:
        n = len(queue)

        for _ in range(n):
            nBus, stop, bus = heapq.heappop(queue)

            if stop == T:
                return nBus

            for next_stop, next_bus in graph[stop]:
                if next_bus != bus:
                    if (next_stop, next_bus) not in visited.keys() or (nBus + 1) < visited[(next_stop, next_bus)]:
                        heapq.heappush(queue, (nBus + 1, next_stop, next_bus))
                        visited[(next_stop, next_bus)] = nBus + 1

                else:
                    if (next_stop, next_bus) not in visited.keys() or (nBus) < visited[(next_stop, next_bus)]:
                        heapq.heappush(queue, (nBus, next_stop, next_bus))
                        visited[(next_stop, next_bus)] = nBus

    return -1



routes = [[1, 2, 7],[2, 9, 5],[3, 5, 11],[8, 4, 3], [6, 4, 12]]
S = 1
T = 12
print(numBusesToDestination(routes, S, T))

