import collections

import treeNode
def rightView(root):
    if not root:
        return []

    q = collections.deque()
    q.append([1, root])
    res = []
    mx_level = 0
    while q:
        if q[-1][0] > mx_level:
            mx_level = q[-1][0]
            res.append([q[-1][1].val])
        level, node = q.pop()
        if node.left:
            q.append([level + 1, node.left])
        if node.right:
            q.append([level + 1, node.right])

    return res

root = treeNode.TreeNode(1)
root.left = treeNode.TreeNode(2)
root.right = treeNode.TreeNode(3)
root.right.right = treeNode.TreeNode(6)
root.left.left = treeNode.TreeNode(4)
root.left.right = treeNode.TreeNode(5)
root.left.right.left = treeNode.TreeNode(7)
root.left.right.left.right = treeNode.TreeNode(9)
print(rightView(root))
