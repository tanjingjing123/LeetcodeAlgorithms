import treeNode

def findDuplicateSubtrees(root):
    memo = set()
    ans = []
    added = set()

    def postorder(root):
        if not root: return "e"  # e => end

        left = postorder(root.left)
        right = postorder(root.right)

        cur = left + right + str(root.val)  # post-order
        if cur in memo and cur not in added:
            ans.append(root)
            added.add(cur)
        else:
            memo.add(cur)
        return cur

    postorder(root)
    return ans

root = treeNode.TreeNode(1)
root.left = treeNode.TreeNode(2)
root.right = treeNode.TreeNode(3)
root.left.left = treeNode.TreeNode(4)
root.right.left = treeNode.TreeNode(2)
root.right.left.left = treeNode.TreeNode(4)
root.right.right = treeNode.TreeNode(4)
print(findDuplicateSubtrees(root))