from collections import defaultdict,Counter

def isPossible(nums):
    freq = defaultdict(int)
    hypo = defaultdict(int)

    for i in nums:
        freq[i] += 1

    for i in nums:
        if freq[i] == 0:
            continue
        if hypo[i] > 0:
            hypo[i] -= 1
            hypo[i+1] += 1
            freq[i] -= 1
        elif freq[i] > 0 and freq[i+1] > 0 and freq[i+2] > 0:
            freq[i] -= 1
            freq[i+1] -= 1
            freq[i+2] -= 1
            hypo[i+3] += 1
        else:
            return False
    return True



nums = [1,2,3,4,4,5,5,6]
print(isPossible(nums))