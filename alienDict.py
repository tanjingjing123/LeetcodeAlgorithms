import collections
def alienOrder(words):
    degree = {key: 0 for key in set(''.join(words))}
    edges = collections.defaultdict(set)
    for pair in zip(words, words[1:]):
        for c1, c2 in zip(*pair):
            if c1 != c2:
                if c2 not in edges[c1]:
                    degree[c2] += 1
                edges[c1].add(c2)
                break

    queue = collections.deque(filter(lambda key: not degree[key], degree.keys()))

    result = []
    while queue:
        letter = queue.popleft()
        result.append(letter)
        for lower_letter in edges[letter]:
            degree[lower_letter] -= 1
            if not degree[lower_letter]:
                queue.append(lower_letter)

    return ''.join(result) if len(result) == len(degree) else ''


words = [
  "wrt",
  "wrf",
  "er",
  "ett",
  "rftt"
]

print(alienOrder(words))