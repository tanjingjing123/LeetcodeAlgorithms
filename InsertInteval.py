def insert(intervals, newInterval):
    lo = 0
    hi = len(intervals) - 1
    left_idx = len(intervals)
    right_idx = -1
    while lo <= hi:
        mid = (lo + hi) // 2
        if newInterval[0] <= intervals[mid][1] and (mid == 0 or newInterval[0] > intervals[mid-1][1]):
            left_idx = mid
            break
        elif newInterval[0] > intervals[mid][1]:
            lo = mid + 1
        else:
            hi = mid - 1

    lo = 0
    hi = len(intervals) - 1
    while lo <= hi:
        mid = (lo + hi) // 2
        if newInterval[1] >= intervals[mid][0] and (mid == len(intervals) - 1 or newInterval[1] < intervals[mid+1][0]):
            right_idx = mid
            break
        elif newInterval[1] < intervals[mid][0]:
            hi = mid - 1
        else:
            lo = mid + 1

    if left_idx > right_idx:
        return intervals[:left_idx] + [newInterval] + intervals[right_idx+1:]
    return intervals[:left_idx] + [[min(intervals[left_idx][0], newInterval[0]), max(intervals[right_idx][1], newInterval[1])]] + intervals[right_idx+1:]

intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]
print(insert(intervals, newInterval))