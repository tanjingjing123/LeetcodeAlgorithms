import node
def copyRandomList(head):
    if not head:
        return None

    root = head
    while head:
        away = head.next
        head.next = node.Node(head.val, away)
        head = head.next.next

    head = root
    while head:
        dummy = head.next
        dummy.random = head.random.next if head.random else None

        head = head.next.next

    dummyhead = root.next
    dummyroot = dummyhead
    while dummyhead and dummyhead.next:
        dummyhead.next = dummyhead.next.next
        dummyhead = dummyhead.next

    dummyhead.next = None

    return dummyroot

head = node.Node(7)
head.next = node.Node(13)
head.next.next = node.Node(11)
head.next.next.next = node.Node(10)
head.next.next.next.next = node.Node(1)
head.random = None
head.next.random = head
head.next.next.random = head.next.next.next.next

