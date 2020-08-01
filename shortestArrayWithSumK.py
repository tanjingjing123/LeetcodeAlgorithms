import collections

def shortestSubarray(A, K):
    n = len(A)
    presum = [0] * (n+1)

    for i in range(1, n+1):
        presum[i] = presum[i-1] + A[i-1]

    deque = collections.deque([])
    res = float("inf")
    for i in range(n+1):
        while deque and presum[i] - presum[deque[0]] >= K:
            res = min(res, i - deque[0])
            deque.popleft()
        while deque and presum[i] <= presum[deque[-1]]:
            deque.pop()
        deque.append(i)

    return res if res != float("inf") else -1

A = [2, 3, -4, 3, 3, -4, 6, -1, -3, 4]
k = 8
print(shortestSubarray(A, k))