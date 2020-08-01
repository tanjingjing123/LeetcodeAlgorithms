import treeNode
def inorderSuccessor(root, p):

    stack = []
    prev = None
    cur = None
    while root or stack:
        while root:
            stack.append(root)
            root = root.left
        root = stack.pop()
        prev = cur
        cur = root
        if prev and prev.val == p.val:
            return cur
        root = root.right


root = treeNode.TreeNode(5)
root.left = treeNode.TreeNode(3)
root.right = treeNode.TreeNode(8)
p = root.right.left = treeNode.TreeNode(7)
root.right.right = treeNode.TreeNode(9)
root.left.left = treeNode.TreeNode(2)
root.left.right = treeNode.TreeNode(4)
print(inorderSuccessor(root, p))