class PeekingIterator:
    def __init__(self, iterator):
        self.iterator = iterator
        self.cur = None



    def peek(self):
        if not self.cur:
            self.cur = self.iterator.next()
        return self.cur


    def next(self):
        if not self.cur:
            self.cur = self.iterator.next()
        v = self.cur
        self.cur = None
        return v


    def hasNext(self):
        if not self.cur and not self.iterator.hasNext():
            return False
        return True

nums = [1, 2, 3]
iter = PeekingIterator(nums)
while iter.hasNext():
    val = iter.peek()
    iter.next()

