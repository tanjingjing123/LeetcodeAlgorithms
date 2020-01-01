import bisect

class commodity:
    def __init__(self, id, weight):
        self._id = id
        self._weight = weight

    def getId(self):
        return self._id

    def getWeight(self):
        return self._weight



class CyberTruck:
    def __init__(self):
        self._currentWeight = 0
        self._commodityMap = {}
        self.timeWeightMap = {0:0}
        self.timestampList = [0]


    def load(self,Commodity, timestamp):
        id = commodity.getId(Commodity)
        self._commodityMap[id] = Commodity
        self._currentWeight += commodity.getWeight(Commodity)
        if self.timestampList[-1] != timestamp:
            self.timestampList.append(timestamp)
        self.timeWeightMap[timestamp] = self._currentWeight

    def unload(self, id, timestamp):
        commodity = self._commodityMap.get(id, None)
        if not commodity:
            return
        del self._commodityMap[id]
        self._currentWeight -= commodity.getWeight()
        if self.timestampList[-1] != timestamp:
            self.timestampList.append(timestamp)
        self.timeWeightMap[timestamp] = self._currentWeight

    def getTotalWeight(self, timestamp):
        if timestamp in self.timeWeightMap:
            return self.timeWeightMap[timestamp]
        return self.search(timestamp)


    def search(self, timestamp):
        idx = bisect.bisect_left(self.timestampList, timestamp)
        return self.timeWeightMap[self.timestampList[idx - 1]]



p1 = commodity(1, 2)
p2 = commodity(2, 3)
p3 = commodity(3, 4)
p4 = commodity(4, 2)
p5 = commodity(5, 5)
p6 = commodity(6, 7)
p7 = commodity(7, 1)
p8 = commodity(8, 1)
p9 = commodity(9, 3)

t = CyberTruck()
t.load(p1, 1)
t.load(p2, 2)
t.load(p3, 5)
t.load(p4, 7)
t.unload(p3.getId(), 7)
t.unload(p2.getId(), 8)
t.unload(p1.getId(), 9)
t.load(p5, 12)
t.load(p6, 15)
t.load(p7, 17)
t.load(p8, 18)
t.load(p9, 19)


for i in range(20):
    print("weight at time " + str(i) + " : " + str(t.getTotalWeight(i)))



