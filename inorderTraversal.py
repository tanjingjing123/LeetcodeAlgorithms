import treeNode
class solution:
    def inorder(self, root):
        if root is None:
            return []
        left, right = self.inorder(root.left), self.inorder(root.right)
        return left + [root.val] + right