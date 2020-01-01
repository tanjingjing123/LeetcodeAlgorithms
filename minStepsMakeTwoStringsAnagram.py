import collections


def minSteps(s, t):
    char_count = {}
    for c in s:
        char_count[c] = 1 if c not in char_count else char_count[c] + 1

    count = 0
    for c in t:
        if c not in char_count or char_count[c] == 0:
            count += 1
        else:
            char_count[c] = char_count[c] - 1

    return count


s = "leetcode"
t = "practice"
print(minSteps(s, t))