import treeNode
class solution:
    def __init__(self):
        self.memo = {1: [treeNode.TreeNode(0)]}

    def allPossibleFBT(self, N):
        if N % 2 == 0: return []
        if N not in self.memo:
            res = []
            for i in range(1, N, 2):
                for left in self.allPossibleFBT(i):
                    for right in self.allPossibleFBT(N - 1 - i):
                        root = treeNode.TreeNode(0)
                        root.left = left
                        root.right = right
                        res.append(root)
            self.memo[N] = res
        return self.memo[N]

obj = solution()
print(obj.allPossibleFBT(7))