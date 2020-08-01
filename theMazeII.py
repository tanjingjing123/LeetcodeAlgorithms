import heapq
def shortestDistance(maze, start, destination):
    if not maze or len(maze[0]) == 0:
        return -1

    m = len(maze)
    n = len(maze[0])

    min_heap = [(0, start[0], start[1])]
    visited = set()

    while min_heap:
        cur_dist, x, y = heapq.heappop(min_heap)
        if [x, y] == destination:
            return cur_dist

        if (x, y) in visited:
            continue

        visited.add((x, y))

        for dx, dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            next_x = x
            next_y = y

            l = 0
            while 0 <= next_x + dx < m and 0 <= next_y + dy < n and maze[next_x + dx][next_y + dy] == 0:
                next_x += dx
                next_y += dy
                l += 1
            heapq.heappush(min_heap, (cur_dist + l, next_x, next_y))

    return -1

maze = [[0, 0, 1, 0, 0], [0, 0, 0, 0, 0],[0, 0, 0, 1, 0],[1, 1, 0, 1, 1],[0, 0, 0, 0, 0]]
start = [0, 4]
destination = [4, 4]
print(shortestDistance(maze, start, destination))