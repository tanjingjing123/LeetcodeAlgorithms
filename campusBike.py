def assignBikes(workers, bikes):
    def dist(p1, p2):
        return abs(p1[0]-p2[0]) + abs(p1[1]-p2[1])

    N = len(workers)
    M = len(bikes)
    distances = []
    for i in range(N):
        for j in range(M):
            distances.append((dist(workers[i], bikes[j]), i, j))

    distances.sort()
    assigned = set()
    result = {}
    for dist, worker, bike in distances:
        if bike not in assigned:
            if worker not in result:
                result[worker] = bike
                assigned.add(bike)

    result = {k: result[k] for k in sorted(result)}
    return result.values()


workers = [[0,0],[1,1],[2,0]]
bikes = [[1,0],[2,2],[2,1]]
print(assignBikes(workers, bikes))