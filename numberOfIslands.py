class solution:
    def numOfIslands(self, grid):
        if not grid:
            return 0
        nr, nc = len(grid), len(grid[0])
        ones = set()
        for i in range(nr):
            for j in range(nc):
                if grid[i][j] == "1":
                    ones.add((i, j))
        moves = [(1, 0), (0, 1),(-1, 0), (0, -1)]
        seen = set()
        num_islands = 0
        for node in ones:
            if node not in seen:
                seen.add(node)
                queue = [node]
                for ele in queue:
                    r, c = ele
                    for dr, dc in moves:
                        row, col = r + dr, c + dc
                        if (row, col) in ones and (row, col) not in seen:
                            queue.append((row, col))
                            seen.add((row, col))
                num_islands += 1
        return num_islands


obj = solution()
grid = [["1","1","0","0","0"],["1","1","0","0","0"], ["0","0","1","0","0"],["0","0","0","1","1"]]
print(obj.numOfIslands(grid))
