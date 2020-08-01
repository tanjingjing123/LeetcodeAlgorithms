import listNode

def reorderList(head):
    if head == None:
        return None
    node = head
    lst = []
    while node:
        lst.append(node)
        node = node.next

    length = len(lst)
    i = 0
    while i < (length // 2):
        lst[i].next = lst[length-i-1]
        lst[length-i-1].next = lst[i+1]
        i += 1
    lst[length//2].next = None

head = listNode.ListNode(1)
head.next = listNode.ListNode(2)
head.next.next = listNode.ListNode(3)
head.next.next.next = listNode.ListNode(4)
head.next.next.next.next = listNode.ListNode(5)
head.next.next.next.next.next = listNode.ListNode(6)
head.next.next.next.next.next.next = listNode.ListNode(7)
head.next.next.next.next.next.next.next = listNode.ListNode(8)
reorderList(head)