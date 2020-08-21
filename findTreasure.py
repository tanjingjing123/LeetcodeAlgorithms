def findAllTreasures(board, start, end):
    if not board:
        return []

    numTreasures = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 1:
                numTreasures += 1

    paths = []
    def dfs(x, y, path, remain):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] == -1 or board[x][y] == 2:
            return
        path.append([x, y])
        temp = board[x][y]
        if temp == 1:
            remain -= 1

        if x == end[0] and y == end[1] and remain == 0:
            paths.append(path[::])
            path.pop()
            board[x][y] = temp
            return
        board[x][y] = 2
        dfs(x + 1, y, path, remain)
        dfs(x - 1, y, path, remain)
        dfs(x, y + 1, path, remain)
        dfs(x, y - 1, path, remain)
        board[x][y] = temp
        path.pop()

    dfs(start[0], start[1], [], numTreasures)
    if len(paths) == 0:
        return []
    index = 0
    minPath = len(paths[0])
    for i in range(1, len(paths)):
        if len(paths[i]) < minPath:
            minPath = min(minPath, len(paths[i]))
            index = i

    return paths[index]

board = [[1, 0, 0, 0, 0],[0, -1, -1, 0, 0],[0, -1, 0, 1, 0],[-1, 0, 0, 0, 0],[0, 1, -1, 0, 0],[0, 0, 0, 0, 0]]
start = [0, 0]
end = [4, 1]
print(findAllTreasures(board, start, end))
