import interval
def employeeFreeTime(schedual):
    work = sorted([[w[0], w[1]] for emp in schedual for w in emp])
    merged_w = [work[0]]
    for w in work[1:]:
        if merged_w[-1][1] < w[0]:
            merged_w.append(w)
        else:
            merged_w[-1][1] = max(merged_w[-1][1], w[1])

    free = []
    for i in range(1, len(merged_w)):
        free.append(interval.Interval(merged_w[i-1][1], merged_w[i][0]))
    return free


schedule = [[[1,3],[6,7]],[[2,4]],[[2,5],[9,12]]]
print(employeeFreeTime(schedule))
