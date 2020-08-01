def longestIncreasingPath(matrix):
    if not matrix or not matrix[0]:
        return 0

    dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    memo = {}

    def dfs(r, c):

        if (r, c) in memo:
            return memo[(r, c)]

        ans = 1
        for ro, co in dirs:
            if 0 <= (r + ro) < R and 0 <= (c + co) < C:
                if matrix[r + ro][c + co] > matrix[r][c]:
                    ans = max(ans, dfs(r + ro, c + co) + 1)

        memo[(r, c)] = ans
        return ans

    R = len(matrix)
    C = len(matrix[0])

    for row in range(R):
        for col in range(C):
            dfs(row, col)

    return max(memo.values())

matrix = [[3,4,5],[3,2,6],[2,2,1]]
print(longestIncreasingPath(matrix))