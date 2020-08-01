import collections


def shortestBridge(A):
    def dfs(i, j, queue):
        if i < 0 or i >= len(A) or j < 0 or j >= len(A[0]) or A[i][j] != 1:
            return
        A[i][j] = 2
        queue.append((i, j))
        dfs(i + 1, j, queue)
        dfs(i - 1, j, queue)
        dfs(i, j + 1, queue)
        dfs(i, j - 1, queue)

    found = False
    queue = collections.deque()
    # only need to find the first island
    for i in range(len(A)):
        for j in range(len(A[0])):
            if A[i][j]:
                dfs(i, j, queue)
                found = True
                break
        if found:
            break


    steps = 0
    dirs = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    visited = set()
    while queue:
        for _ in range(len(queue)):
            row, col = queue.popleft()
            for d in dirs:
                r = row + d[0]
                c = col + d[1]
                if 0 <= r < len(A) and 0 <= c < len(A[0]) and (r, c) not in visited:
                    visited.add((r, c))
                    queue.append((r, c))
                    if A[r][c] == 1:
                        return steps
        steps += 1
    return -1


A = [[1,1,1,1,1],[1,0,0,0,1],[1,0,1,0,1],[1,0,0,0,1],[1,1,1,1,1]]
print(shortestBridge(A))