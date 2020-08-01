class solution:
    def maxArea(self, grid):
        max_value = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    square = self.find_island_square(grid, i, j)
                    max_value = max(max_value, square)
        return max_value

    def find_island_square(self, grid, i, j):
        square = 1
        grid[i][j] = 0
        print(i, j)
        if j > 0 and grid[i][j-1] == 1:
            square += self.find_island_square(grid, i, j - 1)
        if j < len(grid[0]) - 1 and grid[i][j + 1] == 1:
            square += self.find_island_square(grid, i, j + 1)

        if i < len(grid) - 1 and grid[i + 1][j] == 1:
            square += self.find_island_square(grid, i + 1, j)
        if i > 0 and grid[i - 1][j] == 1:
            square += self.find_island_square(grid, i - 1, j)

        return square

obj = solution()
grid = [[0,0,1,0,0,0,0,1,0,0,0,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,1,1,0,1,0,0,0,0,0,0,0,0],
 [0,1,0,0,1,1,0,0,1,0,1,0,0],
 [0,1,0,0,1,1,0,0,1,1,1,0,0],
 [0,0,0,0,0,0,0,0,0,0,1,0,0],
 [0,0,0,0,0,0,0,1,1,1,0,0,0],
 [0,0,0,0,0,0,0,1,1,0,0,0,0]]
print(obj.maxArea(grid))