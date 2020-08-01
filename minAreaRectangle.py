def minAreaRect(points):
    hashmap = {}
    for x, y in points:
        if x not in hashmap:
            hashmap[x] = set()
        hashmap[x].add(y)

    res = 99999999
    for x1, y1, in points:
        for x2, y2 in points:
            if x1<x2 and y1<y2:
                dx, dy = x2-x1, y2-y1
                if y1 in hashmap[x2] and y2 in hashmap[x1]:
                    res = min(res, dx*dy)
    return res if res!= 99999999 else 0

points = [[1,1],[1,3],[3,1],[3,3],[4,1],[4,3]]
print(minAreaRect(points))