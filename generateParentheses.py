def generateParenthesis(n):
    ret = []
    def helper(left, right, temp):
        if left == 0 and right == 0:
            ret.append(temp)
            return
        if left > 0:
            helper(left - 1, right, temp + "(")
        if right > left and right > 0:
            helper(left, right - 1, temp + ")")


    helper(n, n, "")
    return ret

print(generateParenthesis(3))