import collections

def eventualSafeNodes(graph):
    n = len(graph)
    state = [0 for _ in range(n)]
    def dfs(node):
        if state[node] == 1:
            return True
        if state[node] == 2:
            return False
        if state[node] == 0:
            state[node] = 1
            reach_circle = any(dfs(next_node) for next_node in graph[node])
            state[node] = 1 if reach_circle else 2
            return reach_circle

    for node in range(n):
        if state[node] == 0:
            dfs(node)
    return [node for node in range(n) if state[node] == 2]

graph = [[1,2],[2,3],[5],[0],[5],[],[]]
print(eventualSafeNodes(graph))
