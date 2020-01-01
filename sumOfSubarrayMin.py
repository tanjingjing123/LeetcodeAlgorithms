def sumSubarrayMins(a):
    MOD = 10 ** 9 + 7

    stack = []
    ans = dot = 0
    for j, y in enumerate(A):
        # Add all answers for subarrays [i, j], i <= j
        count = 1
        while stack and stack[-1][0] >= y:
            x, c = stack.pop()
            count += c
            dot -= x * c

        stack.append((y, count))
        dot += y * count
        ans += dot
    return ans % MOD

A = [1, 7, 5, 4, 8, 2, 6]
print(sumSubarrayMins(A))
