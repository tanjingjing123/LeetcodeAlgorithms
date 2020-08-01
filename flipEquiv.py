import treeNode
class solution:
    def flipEquiv(self, root1, root2):
        if root1 == None and root2 != None:
            return False
        if root1 != None and root2 == None:
            return False
        if root1 == None and root2 == None:
            return True

        if root1.val == root2.val:
            checkSame = self.flipEquiv(root1.left, root2.left) and self.flipEquiv(root1.right, root2.right)
            checkFlip = self.flipEquiv(root1.left, root2.right) and self.flipEquiv(root1.right, root2.left)
            if checkSame or checkFlip:
                return True
        else:
            return False

root1 = treeNode.TreeNode(1)
root1.left = treeNode.TreeNode(2)
root1.right = treeNode.TreeNode(3)
root1.left.left = treeNode.TreeNode(4)
root1.left.right = treeNode.TreeNode(5)
root1.left.right.left = treeNode.TreeNode(7)
root1.left.right.right = treeNode.TreeNode(8)
root1.right.left = treeNode.TreeNode(6)

root2 = treeNode.TreeNode(1)
root2.left = treeNode.TreeNode(3)
root2.left.right = treeNode.TreeNode(6)
root2.right = treeNode.TreeNode(2)
root2.right.left = treeNode.TreeNode(4)
root2.right.right = treeNode.TreeNode(5)
root2.right.right.left = treeNode.TreeNode(8)
root2.right.right.right = treeNode.TreeNode(7)

mywork = solution()
print(mywork.flipEquiv(root1, root2))


