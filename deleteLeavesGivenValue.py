import treeNode
class solution:
    def removeLeafNodes(self, root, target):
        if root:
            root.left = self.removeLeafNodes(root.left, target)
            root.right = self.removeLeafNodes(root.right, target)
            if root.val == target and not root.left and not root.right:
                return
            else:
                return root


obj = solution()
root = treeNode.TreeNode(1)
root.left = treeNode.TreeNode(2)
root.right = treeNode.TreeNode(3)
root.left.left = treeNode.TreeNode(2)
root.left.right = treeNode.TreeNode(4)
root.right.left = treeNode.TreeNode(2)
root.right.right = treeNode.TreeNode(9)
target = 2
obj.removeLeafNodes(root,target)

