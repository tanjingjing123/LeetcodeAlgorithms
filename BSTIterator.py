import treeNode
class BSTIterator:
    def __init__(self, root):
        self.stack = []
        self.recursiveHelper(root)


    def recursiveHelper(self, node):
        if not node:
            return
        self.recursiveHelper(node.right)
        self.stack.append(node.val)
        self.recursiveHelper(node.left)

    def next(self):
        return self.stack.pop()

    def hasNext(self):
        return len(self.stack) > 0


root = treeNode.TreeNode(7)
root.left = treeNode.TreeNode(3)
root.right = treeNode.TreeNode(15)
root.right.left = treeNode.TreeNode(9)
root.right.right = treeNode.TreeNode(20)
obj = BSTIterator(root)
print(obj.next())
print(obj.next())
print(obj.hasNext())
print(obj.next())
