import doubleListNode
import heapq
def deleteMinPeaks(nums):
    if not nums or len(nums) == 1:
        return nums
    head = doubleListNode.DoubleListNode(nums[0])
    curNode = head
    for i in range(1, len(nums)):
        newNode = doubleListNode.DoubleListNode(nums[i])
        curNode.next = newNode
        newNode.prev = curNode
        curNode = newNode

    h = []
    if head.data > head.next.data:
        heapq.heappush(h, (head.data, head))
    curNode = head.next

    while curNode.next:
        if curNode.data > curNode.prev.data and curNode.data > curNode.next.data:
            heapq.heappush(h, (curNode.data, curNode))

        curNode = curNode.next

    if curNode.data > curNode.prev.data:
        heapq.heappush(h, (curNode.data, curNode))

    res = []
    while h:
        peakval, peakNode = heapq.heappop(h)
        res.append(peakval)
        prevNode = peakNode.prev
        nextNode = peakNode.next
        if prevNode:
            prevNode.next = peakNode.next
            if (not prevNode.prev or prevNode.data > prevNode.prev.data) and (not prevNode.next or prevNode.data > prevNode.next.data):
                heapq.heappush(h, (prevNode.data, prevNode))
        if nextNode:
            nextNode.prev = prevNode
            if (not nextNode.prev or nextNode.data > nextNode.prev.data) and (not nextNode.next or nextNode.data > nextNode.next.data):
                heapq.heappush(h, (nextNode.data, nextNode))

    return res

nums = [2, 7, 8, 5, 1, 6, 3, 9, 4]
print(deleteMinPeaks(nums))


