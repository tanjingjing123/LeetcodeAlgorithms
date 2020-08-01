import listNode
def swapPairs(head):
    if not head:
        return None
    def recur(head):
        if not head or not head.next:
            return head
        third = recur(head.next.next)
        newhead = head.next
        newhead.next = head
        head.next = third
        return newhead
    return recur(head)

head = listNode.ListNode(1)
head.next = listNode.ListNode(2)
head.next.next = listNode.ListNode(3)
head.next.next.next = listNode.ListNode(4)
head.next.next.next.next = listNode.ListNode(5)
head.next.next.next.next.next = listNode.ListNode(6)
head.next.next.next.next.next.next = listNode.ListNode(7)
head.next.next.next.next.next.next.next = listNode.ListNode(8)
head.next.next.next.next.next.next.next.next = listNode.ListNode(9)
print(swapPairs(head))
