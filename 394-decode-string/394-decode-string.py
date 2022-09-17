class Solution(object):
    def decodeString(self, s):
        st, pt = self.decodeHelper(s, 0)
        return st
    
    def decodeHelper(self, s, i):
        res = []
        
        while i < len(s) and s[i] != "]":
            if s[i] in "abcdefghijklmnopqrstuvwxyz":
                res.append(s[i])
            else:
                start = i
                while s[i+1] != "[":
                    i += 1
                x = 0
                partString, j = self.decodeHelper(s, i+2)
                while x < int(s[start:i+1]):
                    res.append(partString)
                    x += 1
                i = j
            i += 1
            
        #[acc, acc, acc]
        return "".join(res), i
            
        
                    
        