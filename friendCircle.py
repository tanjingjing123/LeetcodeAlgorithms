def findCircleNum(M):
    n = len(M)
    res = n
    root = [i for i in range(n)]
    def getRoot(root, i):
        while i != root[i]:
            i = root[i]
            root[i] = root[root[i]]
        return i



    for p in range(n):
        for q in range(p+1, n):
            if M[p][q] == 1:
                root_p = getRoot(root, p)
                root_q = getRoot(root, q)
                if root_p != root_q:
                    res -= 1
                    root[root_q] = root_p
    return res

M = [[1, 1, 0, 1, 0, 0],[1, 1, 1, 0, 0, 0], [0, 1, 1, 0, 0, 0], [1, 0, 0, 1, 0, 0], [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]
print(findCircleNum(M))