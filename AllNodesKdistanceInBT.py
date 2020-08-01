import treeNode
def distance(root, target, k):
    memo = {}
    def prefixLen(A, B):
        i = 0
        for a, b in zip(A, B):
            if a != b:
                break
            i += 1
        return i

    def label(root, tag):
        if not root:
            return None
        memo[tag] = root.val
        l = label(root.left, tag + '0')
        r = label(root.right, tag + '1')
        return tag if root.val == target.val else l or r

    tag = label(root, '1')
    return [memo[a] for a in memo if len(tag) + len(a) - 2 * prefixLen(tag, a) == k]

root = treeNode.TreeNode(3)
target = root.left = treeNode.TreeNode(5)
root.right = treeNode.TreeNode(1)
root.left.left = treeNode.TreeNode(6)
root.left.right = treeNode.TreeNode(2)
root.left.right.left = treeNode.TreeNode(7)
root.left.right.right = treeNode.TreeNode(4)
root.right.left = treeNode.TreeNode(0)
root.right.right = treeNode.TreeNode(8)
print(distance(root, target , 2))
