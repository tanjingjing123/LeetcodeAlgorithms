import collections
import heapq
def findItinerary(tickets):
    g = collections.defaultdict(list)
    for ticket in tickets:
        heapq.heappush(g[ticket[0]], ticket[1])

    def dfs(g, start, res):
        while len(g[start]) != 0:
            dfs(g, heapq.heappop(g[start]), res)
        res.append(start)

    res = []
    dfs(g, "JFK", res)
    return res[::-1]

tickets = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
print(findItinerary(tickets))