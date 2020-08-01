import treeNode
def sortedArrayToBST(nums):
    def buildBST(l, r):
        if l > r:
            return None
        m = l + (r - l) // 2
        root = treeNode.TreeNode(nums[m])
        root.left = buildBST(l, m - 1)
        root.right = buildBST(m + 1, r)

        return root
    return buildBST(0, len(nums) - 1)

nums = [-10, -3, 0, 5, 9]
resultTree = sortedArrayToBST(nums)
def printTreeInorder(root):
    if root:
        printTreeInorder(root.left)
        print(root.val)
        printTreeInorder(root.right)

printTreeInorder(resultTree)