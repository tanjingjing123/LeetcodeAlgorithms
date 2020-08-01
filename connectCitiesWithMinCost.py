def minCost(N, connections):
    if len(connections) < N - 1:
        return -1
    connections.sort(key= lambda i: i[2])
    union = [i for i in range(N + 1)]
    res = 0

    def find(i):
        while i != union[i]:
            union[i] = union[union[i]]
            i = union[i]
        return i

    def connect(i, j):
        if find(i) == find(j):
            return False
        union[find(i)] = find(j)
        return True

    for bicity in connections:
        if connect(bicity[0], bicity[1]):
            res += bicity[2]

    return res

N = 3
connections = [[1,2,5],[1,3,6],[2,3,1]]
print(minCost(N, connections))
