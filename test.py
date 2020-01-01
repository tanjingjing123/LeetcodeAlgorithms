class MyStack:
    def __init__(self):
        self.stack = []

    def insertAtBottom(self, e):
        if not self.stack:
            self.stack.append(e)
        else:
            top = self.stack[-1]
            self.stack.pop()
            self.insertAtBottom(e)
            self.stack.append(top)

    def reverseStack(self):
        if self.stack:
            top = self.stack[-1]
            self.stack.pop()
            self.reverseStack()
            self.insertAtBottom(top)

    def sortedInsert(self,e):
        if len(self.stack) == 0 or e > self.stack[-1]:
            self.stack.append(e)
        else:
            tmp = self.stack.pop()
            self.sortedInsert(e)
            self.stack.append(tmp)

    def sortStack(self):
        if self.stack:
            tmp = self.stack.pop()
            self.sortStack()
            self.sortedInsert(tmp)


stack = MyStack()

stack.stack.append(-5)
stack.stack.append(2)
stack.stack.append(13)
stack.stack.append(4)
stack.stack.append(7)
stack.stack.append(0)
stack.stack.append(8)
stack.stack.append(11)
print(stack.stack)

# stack.reverseStack()
stack.sortStack()
print(stack.stack)
