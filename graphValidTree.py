def validTree(n, edges):
    def find_parent(parent, x):
        if parent[x] == -1:
            return x
        return find_parent(parent, parent[x])

    def union(parent, x, y):
        x = find_parent(parent, x)
        y = find_parent(parent, y)
        parent[x] = y

    parent = [-1] * n

    for x, y in edges:
        x = find_parent(parent, x)
        y = find_parent(parent, y)

        if x != y:
            union(parent, x, y)
        else:
            return False

    return True if parent.count(-1) == 1 else False


n = 5
edges = [[0,1], [0,2], [0,3], [1,4]]
print(validTree(n, edges))