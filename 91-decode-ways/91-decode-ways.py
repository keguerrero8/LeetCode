class Solution(object):
    def numDecodings(self, s):
        if len(s) == 1:
            return 1 if s != "0" else 0
        
        ways = [0]*len(s)
        if s[0] != "0":
            ways[0] = 1
            
        for i in range(1, len(s)):
            if s[i] != "0":
                ways[i] += ways[i-1]
            else:
                ways[i] = 0
            sNum = s[i-1:i+1]
            
            if int(sNum) <= 26 and sNum[0] != "0":
                newWays = ways[i-2] if i - 2 >= 0 else 1
                ways[i] += newWays
                
        return ways[-1]