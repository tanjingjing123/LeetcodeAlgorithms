import treeNode

def balanceBST(root):
    vals = []
    def inorderBST(root):
        if not root:
            return None
        inorderBST(root.left)
        vals.append(root.val)
        inorderBST(root.right)
        return vals
    vals = inorderBST(root)
    l = 0
    r = len(vals)

    def buildBST(l, r):
        if l > r:
            return None
        m = l + (r - l) // 2
        root = treeNode.TreeNode(vals[m])
        root.left = buildBST(l, m - 1)
        root.right = buildBST(m + 1, r)

        return root

    return buildBST(0, r - 1)

def printTreeInorder(root):
    if root:
        printTreeInorder(root.left)
        print(root.val)
        printTreeInorder(root.right)
root = treeNode.TreeNode(1)
root.right = treeNode.TreeNode(2)
root.right.right = treeNode.TreeNode(3)
root.right.right.right = treeNode.TreeNode(4)
res = balanceBST(root)
printTreeInorder(res)
