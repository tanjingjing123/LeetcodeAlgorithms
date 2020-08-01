import collections


class solution:
    def slidingPuzzle(self, board):
        deq = collections.deque([[tuple(board[0] + board[1]), 0]])
        memo = set()
        allowed_d = {0: (1, 3), 1: (-1, 1, 3), 2:(-1, 3), 3:(1, -3), 4:(-1, 1, -3), 5: (-1, -3)}
        while deq:
            tfb, moves = deq.popleft()
            if tfb in memo:
                continue

            if tfb == (1, 2, 3, 4, 5, 0):
                return moves
            memo.add(tfb)

            idx_0 = tfb.index(0)
            for d in allowed_d[idx_0]:
                lfb = list(tfb)
                lfb[idx_0], lfb[idx_0 + d] = lfb[idx_0 + d], lfb[idx_0]
                deq.append([tuple(lfb), moves+1])
        return -1


obj = solution()
board = [[4,1,2],[5,0,3]]
print(obj.slidingPuzzle(board))