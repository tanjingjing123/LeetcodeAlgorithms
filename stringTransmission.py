import treeNode


def boundaryOfBinaryTree(root):
    def find_left(node):
        if node:
            res.append(node.val)
        if node.left:
            find_left(node.left)
        elif node.right:
            find_left(node.right)

    def find_leaf(node):
        if not node:
            return None
        l = find_leaf(node.left)
        r = find_leaf(node.right)

        if not l and not r:
            res.append(node.val)
        return node

    def find_right(node):
        if node:
            if node.right:
                find_right(node.right)
            elif node.left:
                find_right(node.left)
            res.append(node.val)

    res = []
    if not root:
        return []
    if not root.left:
        res.append(root.val)
    else:
        find_left(root)
        res.pop()

    if root.left or root.right:
        find_leaf(root)

    if root.right:
        res.pop()
        find_right(root)
        res.pop()
    return res

root = treeNode.TreeNode(1)
root.left = treeNode.TreeNode(2)
root.right = treeNode.TreeNode(3)
root.right.left = treeNode.TreeNode(8)
root.right.right = treeNode.TreeNode(6)
root.left.left = treeNode.TreeNode(4)
root.left.right = treeNode.TreeNode(5)
root.left.right.left = treeNode.TreeNode(7)
root.left.right.right = treeNode.TreeNode(9)
print(boundaryOfBinaryTree(root))

