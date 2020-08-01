import treeNode
def postorder(root):
    if not root:
        return []
    stack, visited = [], {}

    stack.append(root)
    final = []
    while (stack):
        temp = stack[-1]
        if temp.left and temp.left not in visited:
            temp = temp.left
            stack.append(temp)
            visited[temp] = 1

        elif temp.right and temp.right not in visited:
            temp = temp.right
            stack.append(temp)
            visited[temp] = 1

        else:
            a = stack.pop()

            final.append(a.val)

    return final



root = treeNode.TreeNode(3)
root.left = treeNode.TreeNode(5)
root.right = treeNode.TreeNode(1)
root.left.left = treeNode.TreeNode(6)
root.left.right = treeNode.TreeNode(2)
root.left.right.left = treeNode.TreeNode(7)
root.left.right.right = treeNode.TreeNode(4)
root.right.left = treeNode.TreeNode(0)
root.right.right = treeNode.TreeNode(8)
print(postorder(root))