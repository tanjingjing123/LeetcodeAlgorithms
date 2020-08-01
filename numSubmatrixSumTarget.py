from collections import defaultdict
def numSubmatrixSumTarget(matrix, target):
    r, c = len(matrix), len(matrix[0])
    ps = [[0] * (c + 1) for _ in range(r + 1)]
    for i in range(1, r + 1):
        for j in range(1, c + 1):
            ps[i][j] = ps[i-1][j] + ps[i][j-1] - ps[i-1][j-1] + matrix[i-1][j-1]
    count = 0
    for r1 in range(1, r + 1):
        for r2 in range(r1, r + 1):
            h = defaultdict(int)
            h[0] = 1
            for col in range(1, c + 1):
                curr_sum = ps[r2][col] - ps[r1 - 1][col]
                count += h[curr_sum - target]
                h[curr_sum] += 1

    return count

matrix = [[1,0,1,2,4,3],[2,1,0,-1,-2,1],[-1,2,3,1,2,-1],[1,0,1,-1,3,-2]]
print(numSubmatrixSumTarget(matrix, target=8))