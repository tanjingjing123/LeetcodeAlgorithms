import collections
def topKFrequent(words, k):
    counter = collections.Counter(words)
    res = []
    counter = sorted(counter.items(), key=lambda item: (item[1], item[0]), reverse=True)
    for key, val in counter:
        res.append(key)
    return res[:k]

words = ["the", "day", "is", "sunny", "the", "the", "the", "sunny", "is", "is"]
k = 4
print(topKFrequent(words, k))