class LRUCache(object):

    def __init__(self, capacity):
        self.capacity = capacity
        self.currentCap = 0
        self.cache = {}
        self.head = DoubleLinkedListNode(None, None)
        self.tail = DoubleLinkedListNode(None, None)
        self.head.next = self.tail
        self.tail.prev = self.head
        

    def get(self, key):
        if key not in self.cache:
            return -1
        else:
            nodeToRemove = self.cache[key]
            nodeToRemove.removeBindings()
            self.tail.addToEnd(nodeToRemove)
            return nodeToRemove.value
        

    def put(self, key, value):
        if key in self.cache:
            nodeToUpdate = self.cache[key]
            nodeToUpdate.value = value
            nodeToUpdate.removeBindings()
            self.tail.addToEnd(nodeToUpdate)
        else:
            if self.currentCap >= self.capacity:
                nodeToRemove = self.head.next
                nodeToRemove.removeBindings()
                del self.cache[nodeToRemove.key]
            self.cache[key] = DoubleLinkedListNode(key, value)
            self.tail.addToEnd(self.cache[key])
            self.currentCap += 1
            
class DoubleLinkedListNode:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None
        self.prev = None
        
    def removeBindings(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        self.next = None
        self.prev = None
        
    def addToEnd(self, nodeToAdd):
        self.prev.next = nodeToAdd
        nodeToAdd.prev = self.prev
        self.prev = nodeToAdd
        nodeToAdd.next = self
        


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)