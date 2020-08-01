import treeNode
def str2tree(s):
    def dfs(s):
        if not s:
            return None
        start = 0
        while (start < len(s) and s[start] != '('):
            start += 1

        node = treeNode.TreeNode(s[0:start])
        if len(s) == start:
            return node

        l, r = 0, 0
        for i in range(start, len(s)):
            if s[i] == '(':
                l += 1
            if s[i] == ')':
                r += 1
            if l == r:
                break
        node.left = dfs(s[start+1:i])
        node.right = dfs(s[i+2:-1])
        return node


    return dfs(s)

s = "4(2(3)(1))(6(5))"
print(str2tree(s))