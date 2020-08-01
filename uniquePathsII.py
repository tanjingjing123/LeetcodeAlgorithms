class solution:
    def uniquePathsIII(self, grid):
        if not grid or not grid[0]:
            return 0

        self.m = len(grid)
        self.n = len(grid[0])
        nEmpty = 0
        for i in range(self.m):
            for j in range(self.n):
                if grid[i][j] == 0:
                    nEmpty += 1
                if grid[i][j] == 1:
                    i1, j1 = i, j
                if grid[i][j] == 2:
                    self.i2, self.j2 = i, j
        self.move = [(1, 0), (0, 1), (0, -1), (-1, 0)]
        self.num = 0
        self.dfs(grid, i1, j1, nEmpty + 1)
        return self.num

    def dfs(self, grid, i, j, nEmpty):

        if i < 0 or i >= self.m or j < 0 or j >= self.n or grid[i][j] == -1:
            return

        if i == self.i2 and j == self.j2:
            if nEmpty == 0:
                self.num += 1

            return

        grid[i][j] = -1

        for imv, jmv in self.move:
            self.dfs(grid, i + imv, j + jmv, nEmpty - 1)

        grid[i][j] = 0

        return

obj = solution()
grid = [[1,0,0,0],[0,0,0,0],[0,0,0,2]]
print(obj.uniquePathsIII(grid))