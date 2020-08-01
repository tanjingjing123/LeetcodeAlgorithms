import collections
class LRUCache:
    def __init__(self, capacity: int):
        self.values = collections.OrderedDict()
        self.N = capacity

    def get(self, key: int) -> int:
        if key in self.values:
            value = self.values.pop(key)
            self.values[key] = value
            return self.values[key]
        else:
            return -1

    def put(self, key: int, value: int) -> None:
        if key in self.values:
            self.values.pop(key)
        elif len(self.values) == self.N:
            self.values.popitem(last=False)
        self.values[key] = value


obj = LRUCache(2)
obj.put(1, 1)
obj.put(2, 2)
print(obj.get(1))
obj.put(3, 3)
print(obj.get(2))
obj.put(4, 4)
print(obj.get(1))
print(obj.get(3))
print(obj.get(4))