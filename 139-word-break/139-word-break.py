class Solution(object):
    def wordBreak(self, s, wordDict):
        dp = [False for i in range(len(s) + 1)]
        dp[len(s)] = True
        
        for i in range(len(s) - 1, -1, -1):
            for w in wordDict:
                if (i + len(w)) <= len(s) and w == s[i:i+len(w)]:
                    dp[i] = dp[i + len(w)] 
                if dp[i]:
                    break
        return dp[0]
            
        