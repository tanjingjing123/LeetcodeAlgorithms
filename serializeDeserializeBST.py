import treeNode


class Codec:
    def helper(self, root, path):
        if not root:
            path.append("None")
            return
        path.append(str(root.val))
        self.helper(root.left, path)
        self.helper(root.right, path)

    def helper2(self, path):
        if path[0] == "None":
            path.pop(0)
            return
        else:
            root = treeNode.TreeNode(path[0])
            path.pop(0)
            root.left = self.helper2(path)
            root.right = self.helper2(path)
        return root

    def serialize(self, root) -> str:
        path = []
        self.helper(root, path)
        path = ','.join(path)
        return path

    def deserialize(self, data: str):
        path = data.split(",")
        return self.helper2(path)


obj = Codec()
root = treeNode.TreeNode(5)
root.left = treeNode.TreeNode(3)
root.right = treeNode.TreeNode(6)
root.left.left = treeNode.TreeNode(2)
root.left.right = treeNode.TreeNode(4)
root.right.right = treeNode.TreeNode(7)
print(obj.serialize(root))
