import listNode

def getIntersection(headA, headB):
    table = {}
    travA = headA
    while travA:
        table[travA] = travA.val
        travA = travA.next
    travB = headB
    while travB:
        if travB in table:
            return travB
        travB = travB.next
    return None

headA = listNode.ListNode(4)
headA.next = listNode.ListNode(1)
headA.next.next = listNode.ListNode(8)
headA.next.next.next = listNode.ListNode(4)
headA.next.next.next.next = listNode.ListNode(5)

headB = listNode.ListNode(5)
headB.next = listNode.ListNode(0)
headB.next.next = listNode.ListNode(1)
headB.next.next.next = headA.next.next

print(getIntersection(headA, headB).val)

