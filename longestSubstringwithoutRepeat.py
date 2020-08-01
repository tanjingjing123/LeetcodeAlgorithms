import collections

def lengthOfLongestSubstring(s):
    if len(s) <= 1:
        return len(s)
    i = 0
    res = 0
    char_oc = dict()
    for j, c in enumerate(s):
        if c in char_oc and char_oc[c] + 1 > i:
            i = char_oc[c] + 1
        if res < j - i + 1:
            res = j - i + 1
        char_oc[c] = j
    return res
s = "pwasskedfksert"
print(lengthOfLongestSubstring(s))
