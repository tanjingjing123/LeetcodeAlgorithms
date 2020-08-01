import node
import treeNode
def treeToDoublyList(root):
    if not root:
        return root
    stack = []
    head = treeNode.TreeNode(None)
    node = root
    prev = None
    while stack or node:
        while node:
            stack.append(node)
            node = node.left

        node = stack.pop()
        if not head.right:
            head.right = node
        if prev:
            node.left = prev
            prev.right = node
        prev = node
        node = node.right


    head.right.left = prev
    prev.right = head.right


root = treeNode.TreeNode(3)
root.left = treeNode.TreeNode(5)
root.right = treeNode.TreeNode(8)
root.right.left = treeNode.TreeNode(7)
root.right.right = treeNode.TreeNode(9)
root.left.left = treeNode.TreeNode(1)
root.left.right = treeNode.TreeNode(4)
root.left.left.right = treeNode.TreeNode(2)
print(treeToDoublyList(root))