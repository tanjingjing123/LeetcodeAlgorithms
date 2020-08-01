import treeNode
class solution:
    def deleteNode(self, root, key):
        if not root:
            return root

        if root.val > key:
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            root.right = self.deleteNode(root.right, key)

        else:
            if not root.left:
                return root.right
            elif not root.right:
                return root.left

            curr = root.left
            while curr.right:
                curr = curr.right
            root.val = curr.val
            root.left = self.deleteNode(root.left, root.val)
        return root


obj = solution()
root = treeNode.TreeNode(5)
root.left = treeNode.TreeNode(3)
root.right = treeNode.TreeNode(6)
root.left.left = treeNode.TreeNode(2)
root.left.right = treeNode.TreeNode(4)
root.right.right = treeNode.TreeNode(7)
print(obj.deleteNode(root, 3))