import collections
class LFUCache:
    def __init__(self, capacity):
        self.freq2items = {}
        self.item2freq = {}
        self.item2val = {}
        self.capacity = capacity
        self.min_freq = 0

    def get(self, key):
        if key not in self.item2val:
            return -1
        f = self.item2freq[key]
        del self.freq2items[f][key]
        if len(self.freq2items[f]) == 0 and self.min_freq == f:
            self.min_freq += 1
        if f + 1 not in self.freq2items:
            self.freq2items[f+1] = collections.OrderedDict()
        self.freq2items[f+1][key] = None
        self.item2freq[key] += 1
        return self.item2val[key]

    def put(self, key, value):

        if self.capacity == 0:
            return
        if key not in self.item2val:
            if len(self.item2val) == self.capacity:
                item, _ = self.freq2items[self.min_freq].popitem(last=False)
                del self.item2val[item]
                del self.item2freq[item]
            self.item2val[key] = value
            if 1 not in self.freq2items:
                self.freq2items[1] = collections.OrderedDict()
            self.freq2items[1][key] = None
            self.min_freq = 1
            self.item2freq[key] = 1

        else:
            self.item2val[key] = value
            f = self.item2freq[key]
            del self.freq2items[f][key]
            if f == self.min_freq and len(self.freq2items[f]) == 0:
                self.min_freq += 1
            if f + 1 not in self.freq2items:
                self.freq2items[f + 1] = collections.OrderedDict()
            self.freq2items[f+1][key] = None
            self.item2freq[key] = f + 1

obj = LFUCache(3)
obj.put(1, 1)
obj.put(2, 2)
obj.get(1)
obj.get(1)
obj.put(4, 4)
obj.get(4)
obj.put(3, 3)
obj.get(3)
obj.put(5, 5)
print(obj.get(1))
print(obj.get(3))
print(obj.get(5))
obj.put(6, 6)
print(obj.get(5))