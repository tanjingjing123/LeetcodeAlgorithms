class NestedIterator:
    from collections import deque
    def __init__(self, nestedList):
        self.res = []
        self.idx = 0
        def helper(nl, res=[]):
            if nl.isInteger():
                res.append(nl.getInteger())
                return
            for nest_list in nl.getList():
                helper(nest_list, res)

        for nl in nestedList:
            helper(nl, self.res)

    def next(self):
        if not self.hasNext(): return 0
        res = self.res[self.idx];
        self.idx += 1
        return res

    def hasNext(self):

        return self.res and self.idx < len(self.res)

nestedList = [[1,1],2,[1,1], [1,2,3,4],4,[1,2]]
obj = NestedIterator(nestedList)
obj.next()
