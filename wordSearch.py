
def exist(board, word):
    def is_present(board, i, j, count):
        if count == m:
            return True
        if i < 0 or i >= n or j < 0 or j >= n1 or board[i][j] != word[count]:
            return False
        temp = board[i][j]
        board[i][j] = " "
        found = is_present(board, i + 1, j, count + 1) or is_present(board, i, j + 1, count + 1) or is_present(board,i - 1, j, count + 1) or is_present(board, i, j - 1, count + 1)
        board[i][j] = temp
        return found

    m, n, n1 = len(word), len(board), len(board[0])
    for i in range(n):
        for j in range(n1):
            if board[i][j] == word[0]:
                if is_present(board, i, j, 0):
                    return True
    return False

board =[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]
word = "ABCCED"
print(exist(board, word))

