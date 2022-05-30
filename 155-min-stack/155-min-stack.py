class MinStack(object):

    def __init__(self):
        self.stack = []
        self.mins = []
        

    def push(self, val):
        self.stack.append(val)
        if len(self.mins) == 0:
            self.mins.append(val)
        else:
            if val < self.mins[-1]:
                self.mins.append(val)
            else:
                self.mins.append(self.mins[-1])

    def pop(self):
        self.stack.pop()
        self.mins.pop()    
        

    def top(self):
        return self.stack[-1]
        

    def getMin(self):
        return self.mins[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()