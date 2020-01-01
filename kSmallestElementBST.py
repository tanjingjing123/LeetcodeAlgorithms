import treeNode
def kthSmallest(root, k):
    i = 0
    def helper(root, k):
        nonlocal i
        if not root:
            return
        a = helper(root.left, k)
        i += 1
        if i == k:
            return root.val
        b = helper(root.right, k)
        return b if b else a

    return helper(root, k)

root = treeNode.TreeNode(6)
root.left = treeNode.TreeNode(3)
root.right = treeNode.TreeNode(10)
root.left.left = treeNode.TreeNode(2)
root.left.right = treeNode.TreeNode(4)
root.right.left = treeNode.TreeNode(8)
root.right.left.left = treeNode.TreeNode(7)
root.right.left.right = treeNode.TreeNode(9)
root.right.right = treeNode.TreeNode(15)

k = 5
print(kthSmallest(root, k))