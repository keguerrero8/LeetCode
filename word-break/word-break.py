class Solution(object):
    def wordBreak(self, s, wordDict):
        wordBreakArray = [False]*(len(s)+1)
        wordBreakArray[len(s)] = True
        for i in reversed(range(len(s))):
            for w in wordDict:
                if len(w) + i <= len(s) and s[i:i+len(w)] == w:
                    wordBreakArray[i] = wordBreakArray[i+len(w)]
                
                if wordBreakArray[i]:
                    break
        return wordBreakArray[0]
        