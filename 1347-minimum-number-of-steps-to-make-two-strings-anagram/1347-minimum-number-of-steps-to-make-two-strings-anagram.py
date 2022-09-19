class Solution(object):
    def minSteps(self, s, t):
        countS = {}
        for i in s:
            countS[i] = countS.get(i, 0) + 1
        
        for j in t:
            if j in countS and countS[j] > 0:
                countS[j] -= 1
                
        total = 0    
        for count in countS.values():
            total += count
            
        return total
                
        