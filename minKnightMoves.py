import collections

def minknightMoves(x, y):
    if x == 0 and y == 0:
        return 0
    moves = [(2,1),(1,2),(1,-2),(-2,1),(-1,2),(2,-1),(-1,-2),(-2,-1)]
    visited = set()

    queue = collections.deque()
    queue.appendleft((0,0,0))
    visited.add((0,0))

    while queue:
        for i in range(len(queue)):
            startX, startY, steps = queue.pop()
            if startX == abs(x) and startY == abs(y):
                return steps
            for xc, yc in moves:
                nx = startX + xc
                ny = startY + yc

                if (nx, ny) not in visited and nx > -4 and ny > -4:
                    visited.add((nx, ny))
                    queue.appendleft((nx, ny, steps+1))


x = 5
y = 5
print(minknightMoves(x, y))