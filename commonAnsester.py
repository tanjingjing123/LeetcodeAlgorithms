import collections


def findNodesWithZeroOneParent(edges):
    if not edges:
        return []

    result = []
    memo = collections.defaultdict(list)
    parent = collections.defaultdict(list)
    for edge in edges:
        memo[edge[1]].append(edge[0])
        memo[edge[0]].append(0)


    for k, v in memo.items():
        if len(v) == 0 or len(v) == 1:
            result.append(k)

edges = [[1, 4], [1, 5], [2, 5], [3, 6], [6, 7]]
print(findNodesWithZeroOneParent(edges))