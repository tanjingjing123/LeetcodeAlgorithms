def findIdle(intervals):
    intervals.sort()
    i = 1
    while i < len(intervals):
        if intervals[i-1][1] >= intervals[i][0]:
            intervals[i-1][1] = max(intervals[i-1][1], intervals[i][1])
            intervals.pop(i)
        else:
            i += 1
    res = []

    for i in range(len(intervals)-1):
        left = intervals[i][1]
        right = intervals[i+1][0]
        res.append([left, right])
    return res



intervals = [[1,3],[2,6],[8,10],[15,18]]
print(findIdle(intervals))