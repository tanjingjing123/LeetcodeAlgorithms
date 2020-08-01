import itertools


def expressiveWords(S, words):
    groupS = [[key, len(list(arr))] for key, arr in itertools.groupby(S)]
    count = 0
    for word in words:
        groupW = [[key, len(list(arr))] for key, arr in itertools.groupby(word)]
        if len(groupS) != len(groupW):
            continue
        isStreched = True
        for i, (letterS, freqS) in enumerate(groupS):
            letterW, freqW = groupW[i]
            if letterS != letterW or freqW > freqS or (freqS > freqW and freqS < 3):
                isStreched = False
                break
        if isStreched:
            count += 1

    return count

S = "heeellooo"
words = ["hi", "hello", "heo", "heello"]
print(expressiveWords(S, words))