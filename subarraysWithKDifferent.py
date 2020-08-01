from collections import OrderedDict


def subarraysWithKDistinct(A, K):
    ans = l = 0
    od = OrderedDict()
    for i, n in enumerate(A):
        od[n] = i
        od.move_to_end(n)
        while len(od) > K:
            l = od.popitem(last=False)[1] + 1
        if len(od) == K:
            k = next(iter(od.items()))[1]
            ans += k - l + 1
    return ans


A = [7 ,2,1,3,6,1, 1, 2, 1, 1, 1, 4, 5, 3, 2]
K = 4
print(subarraysWithKDistinct(A, K))

