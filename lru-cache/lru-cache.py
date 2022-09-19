class DoublyLLNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
    def removeBindings(self):
        self.next.prev = self.prev
        self.prev.next = self.next
        self.prev = self.next = None
    
    def insertNodeToTail(self, nodeToInsert):
        self.prev.next = nodeToInsert
        nodeToInsert.prev = self.prev
        self.prev = nodeToInsert
        nodeToInsert.next = self

class LRUCache(object):
    def __init__(self, capacity):
        self.capacity = capacity
        self.currentCapacity = 0
        self.cache = {}
        self.LRUHead = DoublyLLNode(None, None)
        self.LRUTail = DoublyLLNode(None, None)
        self.LRUHead.next = self.LRUTail
        self.LRUTail.prev = self.LRUHead

    def get(self, key):
        if key not in self.cache:
            return -1
        self.cache[key].removeBindings()
        self.LRUTail.insertNodeToTail(self.cache[key])
        return self.cache[key].value
        

    def put(self, key, value):
        if key in self.cache:
            self.cache[key].value = value
            self.cache[key].removeBindings()
            self.LRUTail.insertNodeToTail(self.cache[key])
            return
        else:
            if self.currentCapacity >= self.capacity:
                del self.cache[self.LRUHead.next.key]
                self.LRUHead.next.removeBindings()
        self.currentCapacity += 1
        self.cache[key] = DoublyLLNode(key, value)
        self.LRUTail.insertNodeToTail(self.cache[key])

        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)