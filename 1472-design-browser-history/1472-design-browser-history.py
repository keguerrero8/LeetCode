class DoubleLLNode:
    def __init__(self, val):
        self.next = None
        self.prev = None
        self.val = val

class BrowserHistory(object):

    def __init__(self, homepage):
        self.historyPt = DoubleLLNode(homepage)
        

    def visit(self, url):
        self.historyPt.next = DoubleLLNode(url)
        self.historyPt.next.prev = self.historyPt
        self.historyPt = self.historyPt.next
        

    def back(self, steps):
        count = 0
        while self.historyPt.prev and count < steps:
            self.historyPt = self.historyPt.prev
            count += 1
        return self.historyPt.val

    def forward(self, steps):
        count = 0
        while self.historyPt.next and count < steps:
            self.historyPt = self.historyPt.next
            count += 1
        return self.historyPt.val
        


# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)