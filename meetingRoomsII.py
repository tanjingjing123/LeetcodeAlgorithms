import heapq

def minMeetingRooms(intervals):
    intervals.sort(key = lambda x: x[0])

    h = []
    for a, b in intervals:
        if h and h[0] <= a:
            heapq.heappop(h)
        heapq.heappush(h, b)
    return len(h)


intervals = [[0, 30],[5, 10],[15, 20], [7, 11], [12, 19]]
print(minMeetingRooms(intervals))