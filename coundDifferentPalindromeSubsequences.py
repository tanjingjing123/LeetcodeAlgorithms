def countPalindromeSub(S):
    dp = {}
    def recursion(subs):
        if subs not in dp:
            count = 0
            for c in set(subs):
                left, right = subs.find(c), subs.rfind(c)
                count += 1 if left == right else 2 + recursion(subs[left+1:right])
            dp[subs] = count
        return dp[subs]
    res = recursion(S)
    return res % 1000000007

S = 'bcacb'
print(countPalindromeSub(S))