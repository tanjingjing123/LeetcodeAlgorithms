class solution:
    def __init__(self):
        self.memo = [False] * (1000000 - 1)


    def add(self, key):
        self.memo[key] = True


    def remove(self, key):
        self.memo[key] = False

    def contains(self, key):
        return self.memo[key]

obj = solution()
obj.add(1)
obj.add(2)
print(obj.contains(1))
print(obj.contains(3))
obj.add(2)
print(obj.contains(2))
obj.remove(2)
print(obj.contains(2))
