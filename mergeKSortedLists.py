import heapq
import listNode
class solution:
    def mergeKLists(self, lists):
        if not lists:
            return
        pq = []
        for node in lists:
            if node:
                pq.append((node.val, id(node), node))

        heapq.heapify(pq)
        dummy = listNode.ListNode(0)
        curr = dummy
        while pq:
            node.val, node_id, node = heapq.heappop(pq)
            curr.next = node
            curr = curr.next
            if node.next:
                heapq.heappush(pq, (node.next.val, id(node.next),node.next))
                node = node.next
        return dummy


head1 = listNode.ListNode(1)
head1.next = listNode.ListNode(4)
head1.next.next = listNode.ListNode(5)

head2 = listNode.ListNode(1)
head2.next = listNode.ListNode(3)
head2.next.next = listNode.ListNode(4)

head3 = listNode.ListNode(2)
head3.next = listNode.ListNode(3)
head3.next.next = listNode.ListNode(6)

lists = [head1, head2, head3]
obj = solution()
print(obj.mergeKLists(lists))
