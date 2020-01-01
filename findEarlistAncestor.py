import collections


def findEarlistAncestor(pairs, node):
    directParents = collections.defaultdict(list)
    for pair in pairs:
        directParents[pair[1]].append(pair[0])

    curNode = collections.deque([node])
    visited = set()
    while curNode:
        prevNode = collections.deque()
        size = len(curNode)
        while size:
            size -= 1
            curr = curNode.popleft()
            prevNode.append(curr)
            parents = directParents[curr]
            if not parents:
                continue
            for parent in parents:
                if parent in visited:
                    continue
                curNode.append(parent)
                visited.add(parent)

    return prevNode.popleft()






edges = [[1, 3], [2, 3], [3, 6], [5, 6], [5, 7], [4, 5], [4, 8], [8, 10], [11, 2]]
print(findEarlistAncestor(edges, 6))