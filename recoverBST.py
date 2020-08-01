import treeNode
class solution:
    def recoverTree(self, root):
        x = y = prepre = pre = None

        while root:
            if root.left:
                prepre = root.left
                while prepre.right and prepre.right != root:
                    prepre = prepre.right

                if prepre.right is None:
                    prepre.right = root
                    root = root.left
                else:
                    if pre and root.val < pre.val:
                        y = root
                        if x is None:
                            x = pre
                    pre = root

                    prepre.right = None
                    root = root.right
            else:
                if pre and root.val < pre.val:
                    y = root
                    if x is None:
                        x = pre
                pre = root

                root = root.right

        x.val, y.val = y.val, x.val


root = treeNode.TreeNode(3)
root.left = treeNode.TreeNode(5)
root.right = treeNode.TreeNode(8)
root.right.left = treeNode.TreeNode(7)
root.right.right = treeNode.TreeNode(9)
root.left.left = treeNode.TreeNode(1)
root.left.right = treeNode.TreeNode(4)
root.left.left.right = treeNode.TreeNode(2)
obj = solution()
obj.recoverTree(root)
