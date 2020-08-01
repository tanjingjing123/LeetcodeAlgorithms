import collections
import treeNode
class solution:
    def verticalTraversal(self, root):
        levels = collections.defaultdict(list)
        self.helper(root, 0, 0, levels)
        return [[x[1] for x in sorted(level)] for _, level in sorted(levels.items())]


    def helper(self, root, x, depth, levels):
        if not root:
            return
        levels[x].append([depth, root.val])
        self.helper(root.left, x - 1, depth + 1, levels)
        self.helper(root.right, x + 1, depth + 1, levels)



root = treeNode.TreeNode(3)
root.left = treeNode.TreeNode(5)
root.right = treeNode.TreeNode(1)
root.left.left = treeNode.TreeNode(6)
root.left.right = treeNode.TreeNode(2)
root.left.right.left = treeNode.TreeNode(7)
root.left.right.right = treeNode.TreeNode(4)
root.right.left = treeNode.TreeNode(0)
root.right.right = treeNode.TreeNode(8)
obj = solution()
print(obj.verticalTraversal(root))