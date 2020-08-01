import collections


def subarrayDivByK(A, K):
    res = 0
    count = 0
    memo = collections.defaultdict(int)
    memo[0] = 1
    for num in A:
        res += num
        if res % K in memo:
            count += memo[res % K]
        memo[res % K] += 1
    return count


A = [4, 5, 0, -2, -3, 1]
K = 5
print(subarrayDivByK(A, K))
