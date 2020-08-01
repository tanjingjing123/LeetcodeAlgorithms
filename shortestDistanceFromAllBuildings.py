import collections


class solution:
    def shortestDistance(self, grid):
        self.free_spaces = set()
        houses = set()
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 0:
                    self.free_spaces.add((r, c))
                elif grid[r][c] == 1:
                    houses.add((r, c))
        shortest_dis = float("inf")
        house_map = {}
        for house in houses:
            house_dis_map = self.get_dis(house)
            house_map[house] = house_dis_map
        for space in self.free_spaces:
            total_dis = 0
            for house in house_map:
                total_dis += house_map[house][space]
            shortest_dis = min(shortest_dis, total_dis)
        if shortest_dis == float("inf"):
            return -1
        return shortest_dis

    def get_dis(self, house):
        dis_map = {}
        visited = set()
        next_to_explore = collections.deque([(house, 0)])
        dirs = [(0, 1), (0, -1), (-1, 0), (1, 0)]
        while next_to_explore:
            cur_pt, dis = next_to_explore.popleft()
            for dx, dy in dirs:
                neighbor = (cur_pt[0] + dx, cur_pt[1] + dy)
                if neighbor not in visited and neighbor in self.free_spaces:
                    dis_map[neighbor] = dis + 1
                    visited.add(neighbor)
                    next_to_explore.append((neighbor, dis + 1))
        self.free_spaces = visited
        return dis_map


obj = solution()
grid = [[1,0,2,0,1],[0,0,0,0,0],[0,0,1,0,0]]
print(obj.shortestDistance(grid))

