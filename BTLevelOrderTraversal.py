import treeNode
def levelOrder(root):
    import queue
    if not root:
        return []
    q = queue.Queue()
    ans = []

    q.put((0, root))
    while (not q.empty()):
        w, t = q.get()
        if w > len(ans) - 1:
            ans.append([])
        ans[w].append(t.val)

        if t.left:
            q.put((w+1, t.left))
        if t.right:
            q.put((w+1, t.right))
    return ans

root = treeNode.TreeNode(3)
root.left = treeNode.TreeNode(5)
root.right = treeNode.TreeNode(1)
root.left.left = treeNode.TreeNode(6)
root.left.right = treeNode.TreeNode(2)
root.left.right.left = treeNode.TreeNode(7)
root.left.right.right = treeNode.TreeNode(4)
root.right.left = treeNode.TreeNode(0)
root.right.right = treeNode.TreeNode(8)
print(levelOrder(root))