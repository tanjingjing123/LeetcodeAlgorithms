def exist(board, words):
    def dfs(r, c, trie, tmplist):
        if '#' in trie:
            res.add(tmplist)
        if r < 0 or r > m - 1 or c < 0 or c > n - 1 or board[r][c] not in trie:
            return
        tmp = board[r][c]
        board[r][c] = '@'
        for i, j, in [(0, -1), (0, 1), (-1, 0), (1, 0)]:
            dfs(r + i, c + j, trie[tmp], tmplist + tmp)
        board[r][c] = tmp
    trie = {}
    for word in words:
        t = trie
        for ch in word:
            if ch not in t:
                t[ch] = {}
            t = t[ch]
        t['#'] = '#'
    res = set()
    m = len(board)
    n = len(board[0])
    for i in range(m):
        for j in range(n):
            dfs(i, j, trie, '')

    return list(res)

board = [
  ['o','a','a','n'],
  ['e','t','a','e'],
  ['i','h','k','r'],
  ['i','f','l','v']
]
words = ["oath","pea","eat","rain"]
print(exist(board, words))