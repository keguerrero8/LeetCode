class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        upperB = max(piles)
        lowerB = 1
            
        def eatBananasWithRate(rate):
            currentHours = 0
            for val in piles:
                currentHours += math.ceil(val/rate)
            return currentHours
            
        res = max(piles)
        while lowerB <= upperB:
            k = (lowerB + upperB) // 2
            hours = eatBananasWithRate(k)
            if hours <= h:
                res = min(res, k)
                upperB = k - 1
            else:
                lowerB = k + 1
                
        return res
        