import listNode
from collections import deque
def removeNthFromEnd(head, n):
    q = deque()
    cur = head
    count = 0
    if head.next == None:
        return head
    if head.next.next == None and n == 2:
        return head.next
    while cur != None:
        if len(q) > n:
            q.popleft()
        q.append(cur)
        cur = cur.next
        count += 1
    if count == n:
        return head.next
    else:
        prev = q.popleft()
        cur = q.popleft()
        prev.next = cur.next
        return head

head = listNode.ListNode(1)
head.next = listNode.ListNode(2)
head.next.next = listNode.ListNode(3)
removeNthFromEnd(head, 3)

