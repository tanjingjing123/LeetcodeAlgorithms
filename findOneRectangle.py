def findMultipleShapes(board):
    if not board:
        return []
    result = []
    def floodFillDFS(x, y, shape):
        if x < 0 or x >= len(board) or y < 0 or y >= len(board[0]) or board[x][y] == 1:
            return
        board[x][y] = 1
        shape.append([x, y])
        floodFillDFS(x + 1, y, shape)
        floodFillDFS(x - 1, y, shape)
        floodFillDFS(x, y + 1, shape)
        floodFillDFS(x, y - 1, shape)

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                shape = []
                floodFillDFS(i, j, shape)
                result.append(shape)

    return result


image1 = [
  [1, 0, 1, 1, 1, 1, 1],
  [1, 0, 0, 1, 0, 1, 1],
  [0, 1, 1, 0, 0, 0, 1],
  [1, 0, 1, 1, 0, 1, 1],
  [1, 0, 1, 0, 1, 1, 1],
  [1, 0, 0, 0, 0, 1, 1],
  [1, 1, 1, 0, 0, 1, 1],
  [0, 1, 0, 1, 1, 1, 0],
]
print(findMultipleShapes(board=image1))