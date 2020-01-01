def findOneRectangle(board):
    if not board:
        return []

    result = []
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                result.append([i, j])
                height = 1
                width = 1
                while i + height < len(board) and board[i+height][j] == 0:
                    height += 1
                while j + width < len(board[0]) and board[i][j+height] == 0:
                    width += 1
                result.append([i+height-1, j + width - 1])
                break

        if len(result) != 0:
            break

    return result

image1 = [
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
  [1, 0, 0, 0, 0, 1, 0, 0, 1],
  [1, 0, 0, 0, 0, 1, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 0, 0, 1],
  [1, 1, 1, 1, 1, 1, 1, 1, 1],
]
print(findOneRectangle(board=image1))