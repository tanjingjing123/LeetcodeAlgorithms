import bisect
import collections
def numMatchingSubseq(S, words):
    mapping = collections.defaultdict(list)
    for i, c in enumerate(S):
        mapping[c].append(i)

    def check_word(word):
        pre = -1
        for c in word:
            if c not in mapping:
                return 0
            l = mapping.get(c)

            # try find the left most index that we can find a match
            # between string S and word, after the "pre" index of
            # previous char (init as -1, so that bisect(l, -1) = 0)
            index = bisect(l, pre)

            if index >= len(l):
                # it means that we could't find a valid index (that
                # we can use to match this char) in l after "pre"
                return 0

            # update pre using our found index
            pre = l[index]
        return 1
    return sum(check_word(word) for word in words)



S = "abcde"
words = ["a", "bb", "acd", "ace"]
print(numMatchingSubseq(S, words))