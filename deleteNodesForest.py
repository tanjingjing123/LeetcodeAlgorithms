
import treeNode
class solution:
    def delNodes(self, root, to_delete):
        if not root:
            return None
        if not to_delete:
            return [root]

        to_delete = set(to_delete)
        results = []
        if root.val not in to_delete:
            results.append(root)
        self.dfs(root, to_delete, results)
        return results

    def dfs(self, node, to_delete, results):
        if not node:
            return
        n = None

        if node.val in to_delete:
            if node.left and node.left.val not in to_delete:
                results.append(node.left)

            if node.right and node.right.val not in to_delete:
                results.append(node.right)

            self.dfs(node.left, to_delete, results)
            self.dfs(node.right, to_delete, results)
        else:
            n = node
            node.left = self.dfs(node.left, to_delete, results)
            node.right = self.dfs(node.right, to_delete, results)

        return n


obj = solution()
root = treeNode.TreeNode(1)
root.left = treeNode.TreeNode(2)
root.right = treeNode.TreeNode(3)
root.left.left = treeNode.TreeNode(4)
root.left.right = treeNode.TreeNode(5)
root.right.left = treeNode.TreeNode(6)
root.right.right = treeNode.TreeNode(7)
to_delete = [3, 5]
obj.delNodes(root, to_delete)