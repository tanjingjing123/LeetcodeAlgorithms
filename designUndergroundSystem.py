import collections


class UndergroundSystem:
    def __init__(self):
        self.checkInMemo = {}
        self.checkOutMemo = collections.defaultdict(lambda :[0, 0])



    def checkIn(self, id, stationName, t):
        self.checkInMemo[id] = [stationName, t]


    def checkOut(self, id, endStation, t):
        startStation, startTime = self.checkInMemo.pop(id)
        self.checkOutMemo[(startStation, endStation)][0] += (t - startTime)
        self.checkOutMemo[(startStation, endStation)][1] += 1



    def getAverageTime(self, startStation, endStation):
        totalTime, totalTips = self.checkOutMemo[(startStation, endStation)]
        return totalTime / totalTips







obj = UndergroundSystem()

obj.checkIn(10, "Leyton", 3)
obj.checkOut(10, "Paradise", 8)
print(obj.getAverageTime("Leyton", "Paradise"))

obj.checkIn(5, "Leyton", 10)
obj.checkOut(5, "Paradise", 16)
print(obj.getAverageTime("Leyton", "Paradise"))

obj.checkIn(1, "Leyton", 23)
obj.checkOut(1, "Paradise", 38)
print(obj.getAverageTime("Leyton", "Paradise"))

