import heapq
import treeNode
class solution():
    def dfs(self, root, target, h):
        if not root:
            return

        heapq.heappush(h, (abs(target-root.val),root.val))
        self.dfs(root.left, target, h)
        self.dfs(root.right, target, h)

    def closestKvalues(self, root, target, k):
        h = []
        self.dfs(root, target, h)
        res = []
        for _ in range(k):
            res.append(heapq.heappop(h)[1])
        return res

obj = solution()
root = treeNode.TreeNode(4)
root.left = treeNode.TreeNode(2)
root.right = treeNode.TreeNode(5)
root.left.left = treeNode.TreeNode(1)
root.left.right = treeNode.TreeNode(3)
target = 3.714286
k = 2
print(obj.closestKvalues(root, target, k))