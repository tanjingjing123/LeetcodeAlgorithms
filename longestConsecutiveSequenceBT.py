import treeNode
class solution:
    def longestConsecutive(self, root):
        return self.dfs(root)[2]

    def dfs(self, root):
        if not root:
            return 0,0,0

        l_up, l_down, l_answer = self.dfs(root.left)
        r_up, r_down, r_answer = self.dfs(root.right)
        up, down = 1, 1
        if root.left and root.left.val + 1 == root.val:
            up = max(up, l_up + 1)
        if root.right and root.right.val + 1 == root.val:
            up = max(up, r_up + 1)
        if root.left and root.left.val - 1 == root.val:
            down = max(down, l_down + 1)
        if root.right and root.right.val - 1 == root.val:
            down = max(down, r_down + 1)
        return up, down, max(up + down - 1, l_answer, r_answer)



obj = solution()
root = treeNode.TreeNode(5)
root.left = treeNode.TreeNode(4)
root.left.left = treeNode.TreeNode(3)
root.left.right = treeNode.TreeNode(2)
root.left.left.left = treeNode.TreeNode(2)
root.left.left.right = treeNode.TreeNode(4)
root.right = treeNode.TreeNode(6)
root.right.left = treeNode.TreeNode(7)
root.right.right = treeNode.TreeNode(9)
root.right.left.left = treeNode.TreeNode(6)
root.right.left.right = treeNode.TreeNode(8)
print(obj.longestConsecutive(root))
