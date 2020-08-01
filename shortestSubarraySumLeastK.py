import collections

def shortestSubarray(A, K):
    n = len(A)
    prefix = [0 for _ in range(n)]
    prefix[0] = A[0]
    for i in range(1, n):
        prefix[i] = prefix[i-1] + A[i]

    res = float('inf')
    storage = collections.deque([(-1, 0)])

    for j in range(n):
        while (storage and storage[0][1] <= prefix[j] - K):
            res = min(res, j - storage.popleft()[0])

        while (storage and storage[-1][1] >= prefix[j]):
            storage.pop()

        storage.append((j, prefix[j]))

    return -1 if res == float("inf") else res

A = [3,4,-2,1,3,5,-6,1,6,-1,2]
K = 10
print(shortestSubarray(A, K))