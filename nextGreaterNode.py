import listNode
def nextLargerNodes(head):
    list = []
    while head:
        list.append(head.val)
        head = head.next
    n = len(list)
    res = [0] * n
    stack = []
    for i in range(n):
        while stack and list[stack[-1]] < list[i]:
            res[stack.pop()] = list[i]
        stack.append(i)
    return res





head = listNode.ListNode(2)
head.next = listNode.ListNode(1)
head.next.next = listNode.ListNode(5)
head.next.next.next = listNode.ListNode(1)
head.next.next.next.next = listNode.ListNode(9)
head.next.next.next.next.next = listNode.ListNode(2)
head.next.next.next.next.next.next = listNode.ListNode(5)
head.next.next.next.next.next.next.next = listNode.ListNode(1)
print(nextLargerNodes(head))