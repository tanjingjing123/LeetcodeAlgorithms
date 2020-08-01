import collections

def canFinish(numCourses, prerequisites):
    graph = collections.defaultdict(list)
    for pair in prerequisites:
        graph[pair[1]].append(pair[0])

    visited = [False] * numCourses

    def topSort(node, previousNodes = set()):
        visited[node] = True
        previousNodes.add(node)
        for neighbor in graph[node]:
            if neighbor in previousNodes:
                return False
            if visited[neighbor]:
                continue
            res = topSort(neighbor, previousNodes)
            if not res:
                return res

        previousNodes.remove(node)
        return True

    for i in range(numCourses):
        if visited[i]:
            continue
        res = topSort(i)
        if not res:
            return False

    return True



numCourses2 = 6
prerequisites2 = [[0,3],[0,4],[1,4],[1,3],[2,5],[3,2],[5,0]]
print(canFinish(numCourses2, prerequisites2))
