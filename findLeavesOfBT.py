import collections

import treeNode
def findleaves(root):
    res = collections.defaultdict(list)
    def dfs(node, level, res):
        if not node:
            return 0

        leftlevel, rightlevel = 0, 0
        if node.left:
            leftlevel = max(dfs(node.left, level, res), 0)
        if node.right:
            rightlevel = max(dfs(node.right, level, res), 0)

        level = max(leftlevel, rightlevel)
        res[level].append(node.val)
        return level + 1
    dfs(root, -1, res)
    return list(res.values())



root = treeNode.TreeNode(3)
root.left = treeNode.TreeNode(5)
root.right = treeNode.TreeNode(8)
root.right.left = treeNode.TreeNode(7)
root.right.right = treeNode.TreeNode(9)
root.left.left = treeNode.TreeNode(1)
root.left.right = treeNode.TreeNode(4)
root.left.left.right = treeNode.TreeNode(2)
print(findleaves(root))