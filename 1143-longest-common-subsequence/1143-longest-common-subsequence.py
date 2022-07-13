class Solution(object):
    def longestCommonSubsequence(self, text1, text2):
        dp = [[0 for i in range(len(text2) + 1)] for i in range(len(text1) + 1)]
        
        for i in reversed(range(len(text1))):
            for j in reversed(range(len(text2))):
                if text1[i] == text2[j]:
                    dp[i][j] = 1 + dp[i+1][j+1]
                else:
                    dp[i][j] = max(dp[i][j+1], dp[i+1][j])
                
        return dp[0][0]
        