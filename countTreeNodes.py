import treeNode
def countNodes(root):
    def count(node, c):
        c += 1
        if node.left:
            c = count(node.left, c)
        if node.right:
            c = count(node.right, c)
        return c
    c = 0
    if root:
        c = count(root, c)
    return c

root = treeNode.TreeNode(1)
root.left = treeNode.TreeNode(2)
root.right = treeNode.TreeNode(3)
root.left.left = treeNode.TreeNode(4)
root.left.right = treeNode.TreeNode(5)
root.right.left = treeNode.TreeNode(6)
print(countNodes(root))