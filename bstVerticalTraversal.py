import treeNode
import collections
class solution:
    def verticalOrder(self, root):
        if root is None:
            return []
        self.index_dict = collections.defaultdict(list)
        self.bfs([(root, 0)])
        ans = [self.index_dict[i] for i in sorted(self.index_dict.keys())]
        return ans

    def bfs(self, nodes):
        if not nodes:
            return
        next_nodes = []
        for node, index in nodes:
            self.index_dict[index].append(node.val)
            if node.left:
                next_nodes.append((node.left, index - 1))
            if node.right:
                next_nodes.append((node.right, index + 1))
        self.bfs(next_nodes)

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

print(obj.verticalOrder(root))