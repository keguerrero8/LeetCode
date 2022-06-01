class Solution(object):
    def topKFrequent(self, nums, k):
        frequencyHash = {}
        for num in nums:
            frequencyHash[num] = 1 + frequencyHash.get(num, 0)
        
        heap = []
        for key, value in frequencyHash.items():
            heap.append([key, value])
            
        self.createMaxHeap(heap)
        result = []
        
        for i in range(k):
            element = self.getMaxElement(heap)
            result.append(element)
        
        return result
        
    def createMaxHeap(self, heap):
        end = len(heap) - 1
        for i in reversed(range(len(heap))):
            currentIdx = i
            leftChild = 2*currentIdx + 1
            while leftChild <= end:
                rightChild = 2*currentIdx + 2
                if rightChild <= end:
                    childToCompare = leftChild if heap[leftChild][1] > heap[rightChild][1] else rightChild
                else:
                    childToCompare = leftChild
                if heap[childToCompare][1] > heap[currentIdx][1]:
                    heap[childToCompare], heap[currentIdx] = heap[currentIdx], heap[childToCompare]
                    currentIdx = childToCompare
                    leftChild = 2*currentIdx + 1
                else:
                    break
                    
    def getMaxElement(self, heap):
        heap[0], heap[-1] = heap[-1], heap[0]
        el, frequency = heap.pop()
        
        end = len(heap) - 1
        currentIdx = 0
        leftChild = 2*currentIdx + 1
        while leftChild <= end:
            rightChild = 2*currentIdx + 2
            if rightChild <= end:
                childToCompare = leftChild if heap[leftChild][1] > heap[rightChild][1] else rightChild
            else:
                childToCompare = leftChild
            if heap[childToCompare][1] > heap[currentIdx][1]:
                heap[childToCompare], heap[currentIdx] = heap[currentIdx], heap[childToCompare]
                currentIdx = childToCompare
                leftChild = 2*currentIdx + 1
            else:
                break
        
        return el
        
        