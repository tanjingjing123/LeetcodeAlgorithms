import listNode
def reverseBetween(head, m, n):
    curr = head
    l = []
    while curr:
        l.append(curr)
        curr = curr.next
    if m == n:
        return l[0]
    for i in range(n - 1, m - 1, -1):
        l[i].next = l[i - 1]
    l[m - 1].next = l[n] if n < len(l) else None
    if m > 1:
        l[m - 2].next = l[n - 1]
        return l[0]
    else:
        return l[n - 1]

head = listNode.ListNode(1)
head.next = listNode.ListNode(2)
head.next.next = listNode.ListNode(3)
head.next.next.next = listNode.ListNode(4)
head.next.next.next.next = listNode.ListNode(5)
head.next.next.next.next.next  = listNode.ListNode(6)
m = 2
n = 4
reverseBetween(head, m, n)

