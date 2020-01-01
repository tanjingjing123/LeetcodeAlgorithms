import collections


def frequentAccess(records):
    if not records:
        return []

    result = []
    times = {}
    for record in records:
        if record[0] in times:
            times[record[0]].append(int(record[1]))
        else:
            times[record[0]] = [int(record[1])]

    for name, timestamps in times.items():
        timestamps.sort()
        i = 0
        timewindow = collections.deque([timestamps[i]])
        for j in range(1, len(timestamps)):
            if timestamps[j] - timestamps[i] < 60:
                timewindow.append(timestamps[j])
            else:
                timewindow.popleft()
        if len(timewindow) >= 3:
            result.append([name, timewindow])
    return result



records = [['James', '1300'], ['James', '1500'], ['John', '1120'], ['John', '1150'], ['John', '1220'],['John', '1420'], ['Martha', '1600'], ['Martha', '1620'], ['Martha', '1530']]
print(frequentAccess(records))

