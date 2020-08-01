def findDiagonalOrder(nums):
    m = []
    for i, row in enumerate(nums):
        for j, v in enumerate(row):
            if i+j >= len(m):
                m.append([])
            m[i+j].append(v)
    return [v for d in m for v in reversed(d)]

nums = [[1,2,3,4,5],[6,7],[8],[9,10,11],[12,13,14,15,16]]
print(findDiagonalOrder(nums))