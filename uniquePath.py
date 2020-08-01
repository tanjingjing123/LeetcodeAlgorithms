def uniquePathWithObstacles(obstacleGrid):
    if obstacleGrid[0][0] == 1:
        return 0
    dp = [[1]*len(obstacleGrid[0]) for x in range(len(obstacleGrid))]
    for i in range(len(obstacleGrid)):
        for j in range(len(obstacleGrid[0])):
            if obstacleGrid[i][j] == 1:
                dp[i][j] = 0
                continue
            if i==0 and j==0:
                continue
            t1 = 0
            t2 = 0
            if i-1>=0:
                t1 = dp[i-1][j]
            if j-1>=0:
                t2 = dp[i][j-1]
            dp[i][j] = t1 + t2
    return dp[-1][-1]

grid = [
  [0,0,0,0],
  [0,1,0,0],
  [0,1,0,0]
]
print(uniquePathWithObstacles(grid))