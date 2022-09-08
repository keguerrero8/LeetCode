class Solution(object):
    def addBinary(self, a, b):
        la = len(a) - 1
        lb = len(b) - 1
        res = []
        rem = 0
        
        while la >= 0 or lb >= 0:
            
            aVal = int(a[la]) if la >= 0 else 0
            bVal = int(b[lb]) if lb >= 0 else 0
            sumB = aVal + bVal + rem
            rem = 0
            
            if sumB == 2:
                res.append("0")
                rem = 1
            elif sumB == 3:
                res.append("1")
                rem = 1
            else:
                res.append(str(sumB))
            
            la -= 1
            lb -= 1
            
        if rem > 0:
            res.append("1")
            
        l, r = 0, len(res) - 1
        
        while l <= r:
            res[l], res[r] = res[r], res[l]
            l += 1
            r -= 1
        
        return "".join(res)