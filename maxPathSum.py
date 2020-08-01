import treeNode

class solution:

    def maxPathSum(self, root):
        self.max_val = root.val

        def recur_max_gain(root):
            if not root:
                return 0

            left_tree_sum = recur_max_gain(root.left)
            right_tree_sum = recur_max_gain(root.right)

            curr_sum = left_tree_sum + right_tree_sum + root.val

            if left_tree_sum == 0:
                left_tree_sum = float("-inf")

            if right_tree_sum == 0:
                right_tree_sum = float("-inf")

            self.max_val = max(self.max_val, curr_sum, root.val, left_tree_sum, right_tree_sum)

            return max(root.val + left_tree_sum, root.val + right_tree_sum, root.val)

        val = recur_max_gain(root)
        return max(self.max_val, val)

obj = solution()

root = treeNode.TreeNode(-10)
root.left = treeNode.TreeNode(9)
root.right = treeNode.TreeNode(20)
root.left.left = treeNode.TreeNode(5)
root.left.right = treeNode.TreeNode(-6)
root.left.right.left = treeNode.TreeNode(7)
root.left.right.right = treeNode.TreeNode(2)
root.right.left = treeNode.TreeNode(-15)
root.right.left.left = treeNode.TreeNode(2)
root.right.left.right = treeNode.TreeNode(-6)
root.right.right = treeNode.TreeNode(7)
root.right.right.left = treeNode.TreeNode(-5)
root.right.right.right = treeNode.TreeNode(4)

print(obj.maxPathSum(root))




