def maxGold(grid):
    m = len(grid)
    n = len(grid[0])
    moves = [(0, 1), (1, 0), (0, -1), (-1, 0)]

    def helper(i, j):
        bkp = grid[i][j]
        grid[i][j] = 0
        ans = bkp
        for x, y in moves:
            nx, ny = i + x, j + y

            if nx < 0 or nx >= m or ny < 0 or ny >= n or grid[nx][ny] == 0:
                continue
            ans = max(ans, bkp + helper(nx, ny))

        grid[i][j] = bkp
        return ans

    ans = 0
    for i in range(m):
        for j in range(n):
            if grid[i][j]:
                ans = max(ans, helper(i, j))
    return ans

grid = [[1,6,0,1],[5,0,7,2],[3,0,9,0]]
print(maxGold(grid))
