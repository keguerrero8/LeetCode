class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s == "":
            return 0
        charMap = {}
        start = end = 0
        longestIdx = [0,0]

        while end < len(s):
            if s[end] in charMap:
                if charMap[s[end]] >= start:
                    start = charMap[s[end]] + 1
            charMap[s[end]] = end  
            if end - start > longestIdx[1] - longestIdx[0]:
                    longestIdx = [start, end]
            end += 1

        return longestIdx[1] - longestIdx[0] + 1
        