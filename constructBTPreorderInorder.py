import treeNode
class solution:
    def buildTree(self, preorder, inorder):
        if inorder:
            rootVal = preorder.pop(0)
            i = inorder.index(rootVal)
            root = treeNode.TreeNode(rootVal)
            root.left = self.buildTree(preorder, inorder[0:i])
            root.right = self.buildTree(preorder, inorder[i+1:])
            return root

obj = solution()
preorder = [3,9,2,8,25,10,31,5,1]
inorder = [2,9,8,3,10,25,5,31,1]
print(obj.buildTree(preorder, inorder))