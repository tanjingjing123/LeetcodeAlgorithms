import heapq


def maxMinPath(A):
    m = len(A)
    n = len(A[0])
    seen = {(0, 0)}
    fringe = [[-A[0][0], 0, 0]]
    while fringe:
        score, i, j = heapq.heappop(fringe)
        if i == m - 1 and j == n - 1:
            return -score
        for new_i, new_j in map(lambda x:[i + x[0], j + x[1]], [[0, 1], [0, -1], [1, 0], [-1, 0]]):
            if 0 <= new_i < m and 0 <= new_j < n and (new_i, new_j) not in seen:
                seen.add((new_i, new_j))
                heapq.heappush(fringe, [max(score, -A[new_i][new_j]), new_i, new_j])

A = [[3,4,6,3,4],[0,2,1,1,7],[8,8,3,2,7],[3,2,4,9,8],[4,1,2,0,0],[4,6,5,4,3]]
print(maxMinPath(A))