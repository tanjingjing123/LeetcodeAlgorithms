import collections
def leastInterval(tasks, n):
    freq = collections.Counter(tasks)
    max_freq = max(freq.values())
    freq = list(freq.values())
    max_freq_ele_count = 0
    i = 0
    while i < len(freq):
        if freq[i] == max_freq:
            max_freq_ele_count += 1
        i += 1
    ans = (max_freq - 1) * (n + 1) + max_freq_ele_count
    return max(ans, len(tasks))


tasks = ["A","A","A","A","A","A","B","C","D","E","F","G"]
n = 2
print(leastInterval(tasks, n))
