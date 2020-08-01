def wallsAndGates(rooms):
    if not rooms:
        return
    empty = 2147483647
    rows = len(rooms)
    cols = len(rooms[0])

    def helper(row, col, steps, rooms):
        if row > rows - 1 or row < 0 or col > cols - 1 or col < 0:
            return

        if rooms[row][col] >= steps or rooms[row][col] == empty:
            rooms[row][col] = steps
            helper(row + 1, col, steps + 1, rooms)
            helper(row - 1, col, steps + 1, rooms)
            helper(row, col + 1, steps + 1, rooms)
            helper(row, col - 1, steps + 1, rooms)

    for row in range(rows):
        for col in range(cols):
            if rooms[row][col] == 0:
                helper(row, col, 0, rooms)
    return rooms

rooms = [[2147483647, -1, 0, 2147483647], [2147483647, 2147483647, 2147483647, -1],[2147483647, -1, 2147483647, -1], [0, -1, 2147483647, 2147483647]]
print(wallsAndGates(rooms))