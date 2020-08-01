import treeNode

def isValidBST(root):
    if not root:
        return True

    queue = [[root, float("-inf"), float("inf")]]

    while queue:
        cur = queue.pop(0)
        node = cur[0]
        min_val = cur[1]
        max_val = cur[2]

        if node.val <= min_val or node.val >= max_val:
            return False

        if node.left:
            queue.append([node.left, min_val, node.val])

        if node.right:
            queue.append([node.right, node.val, max_val])

    return True

root = treeNode.TreeNode(6)
root.left = treeNode.TreeNode(2)
root.right = treeNode.TreeNode(11)
root.left.left = treeNode.TreeNode(0)
root.left.right = treeNode.TreeNode(4)
root.left.right.left = treeNode.TreeNode(3)
root.left.right.right = treeNode.TreeNode(5)
root.right.left = treeNode.TreeNode(9)
root.right.left.left = treeNode.TreeNode(7)
root.right.left.right = treeNode.TreeNode(10)
root.right.right = treeNode.TreeNode(15)
print(isValidBST(root))