class MyCalender:
    def __init__(self):
        self.k = []

    def book(self, start, end):
        for k, v in self.k:
            if end > k and v > start:
                return False
        self.k.append((start, end))
        return True
obj = MyCalender()
print(obj.book(10, 20))
print(obj.book(15, 25))
print(obj.book(20,30))