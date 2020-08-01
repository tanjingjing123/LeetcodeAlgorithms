def findMaximumXOR(nums):
    result = 0
    trie = {}
    length = max(nums).bit_length()
    for num in nums:
        curr = opposite = trie
        for digit in map(int, f'{num:b}'.zfill(length)):
            curr = curr.setdefault(digit, {})
            opposite = opposite.get(1 - digit) or opposite.get(digit)
        curr['$'] = num
        result = max(result, opposite['$'] ^ num)
    return result

nums = [3, 10, 5, 25, 2, 8]
print(findMaximumXOR(nums))