import collections


def findOrder(numCourses, prerequisites):
    queue = collections.deque()
    graph = [[] for _ in range(numCourses)]
    dependecies = [0] * numCourses
    path = []
    for u, v in prerequisites:
        graph[v].append(u)
        dependecies[u] += 1

    for i, dep in enumerate(dependecies):
        if dep == 0:
            queue.append(i)


    while queue:
        node = queue.popleft()
        path.append(node)
        numCourses -= 1
        for n in graph[node]:
            dependecies[n] -= 1
            if dependecies[n] == 0:
                queue.append(n)

    if not numCourses:
        return path

    return []

n = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(findOrder(n, prerequisites))