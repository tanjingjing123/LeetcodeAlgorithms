def findLength(A, B):
    memo = {}
    maxx = 0
    for i, a in enumerate(A):
        for j, b in enumerate(B):
            if a == b:
                memo[(i, j)] = memo.get((i - 1, j - 1), 0) + 1
                maxx = max(maxx, memo[(i, j)])
    return maxx


A = [1, 6, 7, 2, 5, 1, 4, 9, 3, 7]
B = [7, 3, 8, 1, 6, 2, 5, 1, 4, 5]
print(findLength(A, B))