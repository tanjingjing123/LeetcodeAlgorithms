import heapq
def trapRainWater(heightMap):
    if not heightMap:
        return 0
    n = len(heightMap)
    m = len(heightMap[0])
    h = []
    grid = [[0]*m for _ in range(n)]
    re = 0

    for i in range(n):
        for j in range(m):
            if i == 0 or j == 0 or i == n - 1 or j == m - 1:
                grid[i][j] = 1
                heapq.heappush(h, (heightMap[i][j], i, j))

    dx = [1, 0, -1, 0]
    dy = [0, 1, 0, -1]
    while h:
        curh, i, j = heapq.heappop(h)
        for k in range(4):
            x = i + dx[k]
            y = j + dy[k]
            if x < 0 or y < 0 or x >= n or y >= m:
                continue

            if grid[x][y] == 0:
                grid[x][y] = 1
                if curh > heightMap[x][y]:
                    re += curh - heightMap[x][y]
                    heapq.heappush(h, (curh, x, y))
                else:
                    heapq.heappush(h, (heightMap[x][y], x, y))

    return re


matrix = [
  [1,4,3,2,3,2],
  [3,2,1,1,2,4],
  [3,1,1,2,1,4],
  [2,3,3,2,3,1]
]
print(trapRainWater(matrix))