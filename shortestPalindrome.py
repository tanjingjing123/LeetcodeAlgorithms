class solution:
    def shortestPalindrome(self, s: str) -> str:
        if self.isPalin(s):
            return s
        add = ''
        while not self.isPalin(s):
            add += s[-1]
            s = s[:-1]
        return add + s + add[::-1]


    def isPalin(self, s):
        return s == s[::-1]
obj = solution()
s = "abcd"
print(obj.shortestPalindrome(s))

