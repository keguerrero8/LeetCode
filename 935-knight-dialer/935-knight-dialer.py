class Solution(object):
    def knightDialer(self, n):
        dp = [1]*10
        
        for i in range(1, n):
            prev = dp + []
            
            dp[0] = prev[6] + prev[4]
            dp[1] = prev[6] + prev[8]
            dp[2] = prev[7] + prev[9]
            dp[3] = prev[8] + prev[4]
            dp[4] = prev[3] + prev[9] + prev[0]
            dp[5] = 0
            dp[6] = prev[1] + prev[7] + prev[0]
            dp[7] = prev[2] + prev[6]
            dp[8] = prev[3] + prev[1]
            dp[9] = prev[2] + prev[4]
            
        total = 0
        for val in dp:
            total += val
            
        return total % (10**9 + 7)
            
        