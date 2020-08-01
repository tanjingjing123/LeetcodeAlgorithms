import collections

def isValidSudoku(board):
    rowSet = [set() for _ in range(9)]
    colSet = [set() for _ in range(9)]
    gridSet = [set() for _ in range(9)]
    for i in range(9):
        for j in range(9):
            n = board[i][j]
            if n == '.':
                continue
            if n in rowSet[i] or n in colSet[i] or n in gridSet[(i//3)*3+(j//3)]:
                return False

            rowSet[i].add(n)
            colSet[j].add(n)
            gridSet[(i//3)*3+(j//3)].add(n)
    return True

grid = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
print(isValidSudoku(board=grid))