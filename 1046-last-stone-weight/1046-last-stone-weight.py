class Solution(object):
    def lastStoneWeight(self, stones):
        for i in range(len(stones)):
            stones[i] = 0 - stones[i]
        heapq.heapify(stones)
        
        while len(stones) > 1:
            stoneOne = heapq.heappop(stones)
            stoneTwo = heapq.heappop(stones)
            delta = abs(stoneOne - stoneTwo)
            if delta > 0:
                heapq.heappush(stones, -1*delta)
                
        return abs(stones[0]) if len(stones) else 0
        
        