class Solution(object):
    def reverse(self, x):
        isNegative = False
        if x < 0:
            isNegative = True
            
        MAXINT = 2147483647
        MININT = -2147483648
        x = abs(x)
        res = 0
        
        while x != 0:
            rem = x % 10
            if res > MAXINT//10 or res == MAXINT//10 and rem > 7:
                return 0
            else:
                res = res*10 + rem
            x = x // 10
            
        return res if not isNegative else -1*res