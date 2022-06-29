class Solution(object):
    def minEatingSpeed(self, piles, h):
        upperB = max(piles)
        lowerB = 1
            
        def eatBananasWithRate(rate):
            currentHours = 0
            for val in piles:
                while val > 0:
                    v = val // rate
                    if v == 0:
                        v = 1
                    currentHours += v
                    val -= v*rate
            return currentHours
            
        k = float("inf")
        while lowerB <= upperB:
            mid = (lowerB + upperB) // 2
            hours = eatBananasWithRate(mid)
            if hours <= h:
                k = min(k, mid)
                upperB = mid - 1
            else:
                lowerB = mid + 1
                
        return k
        