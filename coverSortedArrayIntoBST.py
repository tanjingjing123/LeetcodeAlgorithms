import listNode
import treeNode
class solution:
    def sortedListToBST(self, head):
        nums = []
        while head:
            nums.append(head.val)
            head = head.next

        def fn(lo, hi):
            if lo == hi:
                return None
            mid = (lo + hi) // 2
            return treeNode.TreeNode(nums[mid], fn(lo, mid), fn(mid+1, hi))
        return fn(0, len(nums))


head = listNode.ListNode(-10)
head.next = listNode.ListNode(-3)
head.next.next = listNode.ListNode(0)
head.next.next.next = listNode.ListNode(5)
head.next.next.next.next = listNode.ListNode(9)
obj = solution()
print(obj.sortedListToBST(head))
