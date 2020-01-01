import collections


def commonAncestor(pairs, node1, node2):
    if not pairs:
        return False

    for pair in pairs:

    result = []
    memo = collections.defaultdict(list)
    nodes = set()


edges = [  [1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [8, 10]]
print(findNodesWithZeroOneParent(edges))