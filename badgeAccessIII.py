import collections

def frequentAccess(records):
    if not records:
        return []

    for i in range(len(records)):
        records[i][1] = int(records[i][1])
    records.sort(key=lambda x: x[1])

    result = []
    timeMap = collections.defaultdict(collections.deque)
    for record in records:
        name = record[0]
        curTime = record[1]
        while timeMap[name] and len(timeMap[name]) < 3 and timeMap[name][0] <= curTime - 100:
            timeMap[name].popleft()
        timeMap[name].append(curTime)

    for name, times in timeMap.items():
        if len(times) >= 3:
            result.append([name, list(times)])

    return result



records = [['James', '1300'], ['James', '1500'], ['John', '1120'], ['John', '1150'], ['John', '1220'],['John', '1420'], ['Martha', '1600'], ['Martha', '1620'], ['Martha', '1530']]
print(frequentAccess(records))