from collections import defaultdict


def minSemesters(N, relations):
    indegree = defaultdict(int)
    graph = defaultdict(list)

    for start, end in relations:
        graph[start].append(end)
        indegree[end] += 1

    queue = [(i, 0) for i in range(1, N + 1) if indegree[i] == 0]
    visited = set()
    ans = 0

    while queue != []:
        (pre, sem) = queue.pop(0)
        visited.add(pre)
        ans = max(ans, sem)
        for course in graph[pre]:
            indegree[course] -= 1
            if indegree[course] == 0:
                queue.append((course, sem + 1))

    if len(visited) < N:
        return -1
    else:
        return ans + 1

N = 5
relations = [[1,3],[2,3],[3,5],[4,5]]
print(minSemesters(N, relations))