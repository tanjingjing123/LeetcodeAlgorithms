def minTotalDistance(grid):
    def dist(arr, pt):
        d = 0
        for n in arr:
            d += abs(pt - n)
        return d

    rows, cols = [], []

    for r in range(len(grid)):
        for c in range(len(grid[0])):
            if grid[r][c] == 1:
                rows.append(r)
                cols.append(c)

    rows.sort()
    cols.sort()

    return dist(rows, rows[len(rows)//2]) + dist(cols, cols[len(cols)//2])

grid = [[1,0,0,0,0,1,0],[0,1,0,1,0,0,1],[0,0,0,0,1,0,0],[0,0,1,0,0,1,0]]
print(minTotalDistance(grid))