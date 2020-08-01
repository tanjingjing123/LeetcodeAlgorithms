import treeNode

def zigzagLevelOrder(root):
    res = []
    stack = [root]
    left = True
    while stack and root:
        res.append([i.val for i in stack])
        if left:
            stack = [i for node in stack for i in (node.left, node.right) if i][::-1]
            left = False
        else:
            stack = [i for node in stack for i in (node.right, node.left) if i][::-1]
            left = True
    return res

root = treeNode.TreeNode(3)
root.left = treeNode.TreeNode(9)
root.right = treeNode.TreeNode(20)
root.left.left = treeNode.TreeNode(11)
root.left.right = treeNode.TreeNode(12)
root.right.left = treeNode.TreeNode(15)
root.right.right = treeNode.TreeNode(7)
print(zigzagLevelOrder(root))
