import listNode

def addTwoNumber(l1, l2):
    cur1 = l1
    cur2 = l2

    ans = None
    prev = None

    carry = 0
    while cur1 or cur2:
        val1 = cur1.val if cur1 else 0
        val2 = cur2.val if cur2 else 0

        addition = val1 + val2 + carry

        carry = int(addition >= 10)
        node = listNode.ListNode(addition % 10)
        if not ans:
            ans = node
        else:
            prev.next = node
        prev = node

        if cur1:
            cur1 = cur1.next
        if cur2:
            cur2 = cur2.next

    if carry:
        prev.next = listNode.ListNode(1)
    return ans

l1 = listNode.ListNode(2)
l1.next = listNode.ListNode(4)
l1.next.next = listNode.ListNode(3)
l2 = listNode.ListNode(5)
l2.next = listNode.ListNode(6)
l2.next.next = listNode.ListNode(4)
print(addTwoNumber(l1, l2))
