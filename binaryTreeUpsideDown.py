import treeNode
def upsideDown(root):
    if not root:
        return None
    new_root = root
    while new_root.left:
        new_root = new_root.left

    def search(node, new_left=None, new_right = None):
        if not node:
            return
        search(node.left, node.right, node)
        search(node.right, None, None)
        node.left = new_left
        node.right = new_right

    search(root)
    return new_root


root = treeNode.TreeNode(1)
root.left = treeNode.TreeNode(2)
root.right = treeNode.TreeNode(3)
root.right.left = treeNode.TreeNode(8)
root.right.right = treeNode.TreeNode(6)
root.left.left = treeNode.TreeNode(4)
root.left.right = treeNode.TreeNode(5)
root.left.right.left = treeNode.TreeNode(7)
root.left.right.right = treeNode.TreeNode(9)

print(upsideDown(root))