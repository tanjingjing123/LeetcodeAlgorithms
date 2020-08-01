import collections

def seqReconstruction(org, seqs):
    num_set = {x for seq in seqs for x in seq}
    n = len(num_set)
    if n != len(org):
        return False
    indeg = {x: 0 for x in num_set}
    graph = collections.defaultdict(set)
    for lis in seqs:
        for i in range(len(lis) - 1):
            x, y = lis[i], lis[i+1]
            if y not in graph[x]:
                graph[x].add(y)
                indeg[y] += 1

    q = [k for k in indeg if indeg[k] == 0]
    res = []

    while len(q) == 1:
        res.append(q.pop())
        for x in graph[res[-1]]:
            indeg[x] -= 1
            if indeg[x] == 0:
                q.append(x)
    return res == org
org = [4,1,5,2,6,3]
seqs = [[5,2,6,3],[4,1,5,2]]
print(seqReconstruction(org, seqs))