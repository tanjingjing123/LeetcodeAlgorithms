class solution:
    def orangeRotting(self, grid):
        queue = []
        fresh = set()
        rl = len(grid)
        cl = len(grid[0])
        time = -1
        for i in range(rl):
            for j in range(cl):
                if grid[i][j] == 1:
                    fresh.add((i, j))
                if grid[i][j] == 2:
                    queue.append((i, j))

        if len(fresh) == 0:
            return 0

        while len(queue):
            time += 1
            new_q = []
            for r, c in queue:
                if (r + 1, c) in fresh:
                    new_q.append((r + 1, c))
                    fresh.remove((r + 1, c))

                if (r - 1, c) in fresh:
                    new_q.append((r - 1, c))
                    fresh.remove((r - 1, c))

                if (r, c + 1) in fresh:
                    new_q.append((r, c + 1))
                    fresh.remove((r, c + 1))

                if (r, c - 1) in fresh:
                    new_q.append((r, c - 1))
                    fresh.remove((r, c - 1))
            queue = new_q

        return time if len(fresh) == 0 else -1

grid = [[2,1,1],[1,1,0],[0,1,1]]
obj = solution()
print(obj.orangeRotting(grid))




