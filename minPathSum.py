def minPathSum(grid):
    rows, cols = len(grid), len(grid[0])
    for i in range(rows):
        for j in range(cols):
            if i == 0 and j == 0:
                continue
            if i == 0:
                grid[i][j] = grid[i][j] + grid[i][j-1]

            elif j == 0:
                grid[i][j] = grid[i][j] + grid[i-1][j]

            else:
                grid[i][j] = min(grid[i][j-1],grid[i-1][j]) + grid[i][j]
    return grid[rows-1][cols-1]


grid = [
  [1,3,1],
  [1,5,1],
  [4,2,1]
]
print(minPathSum(grid))