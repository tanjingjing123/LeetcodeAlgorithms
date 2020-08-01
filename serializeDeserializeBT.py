from collections import deque

import treeNode
class Codec:
    def serialize(self, root):
        if root is None:
            return "X,"
        return str(root.val) + "," + self.serialize(root.left) + self.serialize(root.right)


    def deserializeHelper(self, queue):
        ele = queue.popleft()
        if ele == 'X':
            return None
        node = treeNode.TreeNode(int(ele))
        node.left = self.deserializeHelper(queue)
        node.right = self.deserializeHelper(queue)
        return node

    def deserialize(self, data):
        queue = deque(data.split(','))
        return self.deserializeHelper(queue)

obj = Codec()
root = treeNode.TreeNode(1)
root.left = treeNode.TreeNode(2)
root.right = treeNode.TreeNode(3)
root.right.left = treeNode.TreeNode(4)
root.right.right = treeNode.TreeNode(5)
print(obj.serialize(root))
