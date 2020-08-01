import collections

import treeNode
def findleaves(root):
    def helper(node, level, res):
        leftlevel, rightlevel = 0, 0
        if node.left:
            leftlevel = max(helper(node.left, level, res), 0)
        if node.right:
            rightlevel = max(helper(node.right, level, res), 0)

        level = max(leftlevel, rightlevel)
        res[level].append(node.val)
        return level + 1
    res = collections.defaultdict(list)
    helper(root, -1, res)
    return (res.values())



root = treeNode.TreeNode(3)
root.left = treeNode.TreeNode(5)
root.right = treeNode.TreeNode(8)
root.right.left = treeNode.TreeNode(7)
root.right.right = treeNode.TreeNode(9)
root.left.left = treeNode.TreeNode(1)
root.left.right = treeNode.TreeNode(4)
root.left.left.right = treeNode.TreeNode(2)
print(findleaves(root))