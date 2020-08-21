import collections
def findPeople(badge_times):
    memo = collections.defaultdict(list)
    for slot in badge_times:
        memo[slot[0]].append(int(slot[1]))

    res = collections.defaultdict(list)
    for person, times in memo.items():
        times.sort()
        lot = collections.deque()
        lot.append(times[0])
        for i in range(1, len(times)):
            lot.append(times[i])
            while times[i] - lot[0] > 100:
                lot.popleft()

            if len(lot) >= 3:
                res[person].append(list(lot))
                break
    return res


badge_times = [["Paul", "1355"],
["Jennifer", "1910"],
["John", "830"],
["Paul", "1315"],
["John", "1615"],
["John", "1640"],
["John", "835"],
["Paul", "1405"],
["John", "855"],
["John", "930"],
["John", "915"],
["John", "730"],
["John", "940"],
["Jennifer", "1335"],
["Jennifer", "730"],
["John", "1630"],
["Jennifer", "5"]]

print(findPeople(badge_times))