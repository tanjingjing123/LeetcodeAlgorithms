class solution:
    def solve(self, board):
        for i in range(len(board)):
            for j in range(len(board[0])):
                if (i == 0 or (i + 1) == len(board) or j == 0 or (j + 1) == len(board[0])) and board[i][j] == "O":
                    self.draw(board, i, j, len(board), len(board[0]))
        for i in range(len(board)):
            for j in range(len(board[0])):
                if board[i][j] == "O":
                    board[i][j] = "X"
                if board[i][j] == "-":
                    board[i][j] = "O"

    def draw(self, board, i, j, il, jl):
        if i < 0 or i >= il or j < 0 or j >= jl or board[i][j] != "O":
            return
        board[i][j] = "-"
        self.draw(board, i - 1, j, il, jl)
        self.draw(board, i + 1, j, il, jl)
        self.draw(board, i, j - 1, il, jl)
        self.draw(board, i, j + 1, il, jl)


obj = solution()
board = [['X','X','X','X','O'], ['X','O','O','X','O'],['X','O','X','O','X'],['X','O','X','X', 'O']]
print(obj.solve(board))
