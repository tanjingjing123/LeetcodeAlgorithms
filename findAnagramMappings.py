def anagramMappings(a, b):
    map = {}
    for i, x in enumerate(b):
        map[x] = i
    res = []
    for num in a:
        res.append(map[num])
    return res

A = [12, 28, 46, 32, 50]
B = [50, 12, 32, 46, 28]
print(anagramMappings(A, B))
