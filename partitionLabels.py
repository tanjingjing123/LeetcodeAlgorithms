def partitionLabels(S):
    arr = S
    hashmap = dict()
    for i, ch in enumerate(arr):
        if ch not in hashmap:
            hashmap[ch] = i
        else:
            hashmap[ch] = i
    start = 0
    end = 0
    res = []
    for i, ch in enumerate(arr):
        end = max(end, hashmap[ch])
        if i == end:
            res.append((end - start + 1))
            start = end + 1
    return res

S = "ababcbacadefegdehijhklij"
print(partitionLabels(S))