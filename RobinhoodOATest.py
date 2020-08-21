import collections
def digitAnagrams(a):
    seenMap = collections.Counter()

    for num in a:
        numStr = str(num)
        numStr = "".join(sorted(numStr))
        seenMap[numStr] += 1

    res = 0
    for key, value in seenMap.items():
        if value > 1:
            res += value * (value - 1) // 2
    return res


a = [35, 25, 872, 228, 53, 278, 872]
print(digitAnagrams(a))