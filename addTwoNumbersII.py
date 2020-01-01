import listNode

def addTwoNum(l1, l2):
    st1 = []
    st2 = []

    while l1:
        st1.append(l1.val)
        l1 = l1.next

    while l2:
        st2.append(l2.val)
        l2 = l2.next

    cur = None
    summ = 0
    while st1 or st2 or summ:
        if st1:
            summ += st1.pop()
        if st2:
            summ += st2.pop()
        node = listNode.ListNode(summ%10)
        node.next = cur
        cur = node
        summ = summ//10
    return cur

l1 = listNode.ListNode(7)
l1.next = listNode.ListNode(2)
l1.next.next = listNode.ListNode(4)
l1.next.next.next = listNode.ListNode(8)
l1.next.next.next.next = listNode.ListNode(5)

l2 = listNode.ListNode(1)
l2.next = listNode.ListNode(6)
l2.next.next = listNode.ListNode(2)
l2.next.next.next = listNode.ListNode(4)

print(addTwoNum(l1, l2))