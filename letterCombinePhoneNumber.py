
def letterCombination(digits):
    l = [0,1,'abc','def','ghi','jkl','mno','pqrs','tuv','wxyz']
    if len(digits) == 0:
        return []
    else:
        curr = l[int(digits[0])]
        for i in range(1, len(digits)):
            d = int(digits[i])
            curr = [(m + n) for m in curr for n in l[d]]
        return curr


digits = "349"
print(letterCombination(digits))