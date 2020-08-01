import collections


def hasPath(maze, start, destination):
    queue = collections.deque()
    queue.append(tuple(start))
    visited = set()
    while queue:
        start = queue.popleft()
        if list(start) == destination:
            return True
        visited.add(start)
        row, col = start
        for r, c in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
            nr, nc = row + r, col + c
            while nr >= 0 and nr < len(maze) and nc >= 0 and nc < len(maze[0]) and maze[nr][nc] != 1:
                nr, nc = nr + r, nc + c
            if (nr - r, nc - c) not in visited:
                queue.append((nr-r, nc-c))
    return False

maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0],[0, 0, 0, 1, 0],[1, 1, 0, 1, 1],[0, 0, 0, 0, 0]]
start = [0, 4]
destination = [4, 4]
print(hasPath(maze, start, destination))