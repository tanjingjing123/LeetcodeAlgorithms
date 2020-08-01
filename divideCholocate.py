def maximizeSweetness(sweetness, K):
    requested_chunks = K + 1
    l, r = 1, sum(sweetness)//(requested_chunks)
    while l <= r:
        m = (l + r) // 2
        chunks = curr = 0
        for sweet in sweetness:
            curr += sweet
            if curr >= m:
                chunks += 1
                curr = 0

        if chunks >= requested_chunks:
            l = m + 1
        else:
            r = m - 1
    return r


nums = [3,6,1,4,2,4,2,3,7,5,3]
K = 4
print(maximizeSweetness(nums, K))