def findReplaceString(S, indexes, sources, targets):
    S = list(S)
    for i, x, y in sorted(zip(indexes, sources, targets), reverse=True):
        if all(i + k < len(S) and S[i + k] == x[k] for k in range(len(x))):
            S[i:i + len(x)] = list(y)

    return "".join(S)

S = "vmokggqzp"
indexes = [3, 5, 1]
sources = ["kg", "ggq", "mo"]
targets = ["s", "so", "bfr"]
print(findReplaceString(S, indexes, sources, targets))
