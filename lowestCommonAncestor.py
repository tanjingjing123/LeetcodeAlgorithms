import treeNode
from treeNode import TreeNode


class solution:
    def lowestCommonAncestor(self, root, p, q):
        if not root:
            return None

        if root.val == p.val or root.val == q.val:
            return root
        l = self.lowestCommonAncestor(root.left, p, q)
        r = self.lowestCommonAncestor(root.right, p, q)

        if l and r:
            return root
        if l:
            return l
        if r:
            return r

        return None


root= treeNode.TreeNode(3)
root.left = treeNode.TreeNode(5)
root.right = treeNode.TreeNode(1)
root.left.left = treeNode.TreeNode(6)
root.left.right = treeNode.TreeNode(2)
p = root.left.right.left = treeNode.TreeNode(7)
root.left.right.right = treeNode.TreeNode(4)
root.right.left = treeNode.TreeNode(0)
q = root.right.right = treeNode.TreeNode(8)
obj = solution()
print(obj.lowestCommonAncestor(root, p, q))
