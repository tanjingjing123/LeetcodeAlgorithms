import collections


def hasCommonAncestors(edges, x, y):
    if not edges:
        return False

    parentX = set()
    parentY = set()
    memo = collections.defaultdict(list)
    for edge in edges:
        memo[edge[1]].append(edge[0])
    newNodeX = [x]
    newNodeY = [y]
    while newNodeX or newNodeY:
        for node in newNodeX:
            if node in parentY:
                return True
            parentX.add(node)
        for node in newNodeY:
            if node in parentX:
                return True
            parentY.add(node)
        nextNewNodeX = []
        for node in newNodeX:
            nextNewNodeX += memo[node]
        newNodeX = nextNewNodeX
        nextNewNodeY = []
        for node in newNodeY:
            nextNewNodeY += memo[node]
        newNodeY = nextNewNodeY

    return False

edges = [  [1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [8, 10]]
print(hasCommonAncestors(edges, 6, 10))