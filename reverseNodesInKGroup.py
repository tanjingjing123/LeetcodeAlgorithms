import listNode
class solution:
    def reverseKGroup(self, head, k):
        if k < 2:
            return head
        node = head
        for i in range(k):
            if not node:
                return head
            node = node.next
        prev = self.reverseKGroup(node, k)

        for i in range(k):
            temp = head.next
            head.next = prev
            prev = head
            head = temp

        return prev


head = listNode.ListNode(1)
head.next = listNode.ListNode(2)
head.next.next = listNode.ListNode(3)
head.next.next.next = listNode.ListNode(4)
head.next.next.next.next = listNode.ListNode(5)
head.next.next.next.next.next = listNode.ListNode(6)
head.next.next.next.next.next.next = listNode.ListNode(7)
obj = solution()
print(obj.reverseKGroup(head, 4))



