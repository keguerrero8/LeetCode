import random

class RandomizedSet(object):

    def __init__(self):
        self.randomSet = {}
        self.values = []

    def insert(self, val):
        if val not in self.randomSet:
            self.values.append(val)
            self.randomSet[val] = len(self.values) - 1
            return True
        return False
        
        

    def remove(self, val):
        if val in self.randomSet:
            if len(self.values) > 1:
                idx = self.randomSet[val]
                newVal = self.values[-1]
                self.values[idx] = newVal
                self.randomSet[newVal] = idx
                
            del self.randomSet[val]
            self.values.pop()
            return True
        return False

    def getRandom(self):
        randomId = random.randint(0, len(self.values) - 1)
        return self.values[randomId]
        


# Your RandomizedSet object will be instantiated and called as such:
# obj = RandomizedSet()
# param_1 = obj.insert(val)
# param_2 = obj.remove(val)
# param_3 = obj.getRandom()

#keep track of total numbers, find random number from total, choose that index from an array or other structure to access that value
#