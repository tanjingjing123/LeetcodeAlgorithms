import collections
def minWindow(s, t):
    counts_s = collections.Counter(s)
    counts_t = collections.Counter(t)

    # validation
    for key, count in counts_t.items():
        if key not in counts_s.keys() or counts_s[key] < count:
            return ""

    window = collections.defaultdict(int)
    j, min_str = 0, s
    required, catchup = len(counts_t), 0
    for i, x in enumerate(s):
        window[x] += 1
        if window[x] == counts_t[x]:
            catchup += 1

        while window[s[j]] > counts_t[s[j]]:
            window[s[j]] -= 1
            j += 1

        if catchup == required and len(min_str) > len(s[j:i + 1]):
            min_str = s[j:i + 1]

    return min_str

S = "ADOBECODEBANC"
T = "ABC"
print(minWindow(S, T))
