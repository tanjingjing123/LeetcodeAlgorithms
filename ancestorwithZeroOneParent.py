import collections


def findNodesWithZeroOneParent(edges):
    if not edges:
        return []

    result = []
    memo = collections.defaultdict(list)
    nodes = set()
    for edge in edges:
        nodes.add(edge[0])
        nodes.add(edge[1])
        if edge[1] not in memo:
            memo[edge[1]] = 1
        else:
            memo[edge[1]] += 1
    result = collections.defaultdict(list)


    for node in nodes:
        if node not in memo.keys():
            result[0].append(node)
        else:
            if memo[node] == 1:
                result[1].append(node)
            else:
                continue
    return list(result.values())

edges = [  [1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [8, 10]]
print(findNodesWithZeroOneParent(edges))