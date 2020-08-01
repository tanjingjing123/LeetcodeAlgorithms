class SnakshotArray:
    def __init__(self, length):
        self.size = length
        self.arr = {}
        self.snap_id = 0
        self.snapMap = {}

    def set(self, index, val):
        if index >= self.size:
            return
        self.arr[index] = val

    def snap(self):
        self.snapMap[self.snap_id] = self.arr.copy()
        self.snap_id += 1
        return self.snap_id - 1

    def get(self, index, snap_id):
        if index in self.snapMap[snap_id].keys():
            return self.snapMap[snap_id][index]
        else:
            return 0