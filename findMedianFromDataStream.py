import heapq
class MedianFinder:
    def __init__(self):
        self.max = []
        self.min = []


    def addNum(self, num):
        if len(self.min) == len(self.max):
            heapq.heappush(self.max, -heapq.heappushpop(self.min, num))
        else:
            heapq.heappush(self.min, -heapq.heappushpop(self.max, -num))



    def findMedian(self):
        if len(self.max) == len(self.min):
            return float(self.min[0] - self.max[0]) / 2.0
        else:
            return float(-self.max[0])

obj = MedianFinder()
obj.addNum(7)
obj.addNum(3)
obj.addNum(10)
obj.addNum(1)
obj.addNum(4)
obj.addNum(3)
print(obj.findMedian())
obj.addNum(9)
obj.addNum(2)
obj.addNum(8)
obj.addNum(8)
print(obj.findMedian())
