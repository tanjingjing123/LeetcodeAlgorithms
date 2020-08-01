import collections


def longestConsecutive(nums):
    if not nums:
        return 0

    def union(node1, node2):
        root1, root2 = find(node1), find(node2)
        if root1 != root2:
            parent[root1] = root2

    def find(node):
        if parent[node] == -1:
            return node
        parent[node] = find(parent[node])
        return parent[node]

    node_id = 0
    nodes = {}
    parent = []
    for num in nums:
        parent.append(-1)
        nodes[num] = node_id
        node_id += 1

    for num in nums:
        if num + 1 in nodes:
            union(nodes[num], nodes[num + 1])

    counter = collections.defaultdict(int)
    for i in range(len(parent)):
        root = find(i)
        counter[root] += 1

    return max(counter.values())


nums = [100, 4, 200, 8, 12, 49, 92, 10, 7, 5, 1, 14, 11, 3, 2]
print(longestConsecutive(nums))