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

    res = []
    n, n1 = len(board), len(board[0])
    for i in range(n):
        for j in range(n1):
            for word in words:
                m = len(word)
                if board[i][j] == word[0]:
                    if is_present(board, i, j, 0):
                        res.append(word)
                        words.remove(word)
    return res

board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
print(exist(board, words))