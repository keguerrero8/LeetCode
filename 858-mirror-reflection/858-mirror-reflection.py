class Solution(object):
    def mirrorReflection(self, p, q):
        while p % 2 == 0 and q % 2 == 0:
            q /= 2
            p /= 2
            
        if p % 2 and q % 2:
            return 1
        
        if p % 2 == 0 and q % 2:
            return 2
        
        if p % 2 and q % 2 == 0:
            return 0
        