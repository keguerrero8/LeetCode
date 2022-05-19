class Solution(object):
    def lengthOfLongestSubstring(self, s):
        if s == "":
            return 0
        longestLength = 0
        hashWords = {}
        start = end = 0

        while end < len(s):
            if s[end] not in hashWords:
                hashWords[s[end]] = end
            else:
                if hashWords[s[end]] >= start:
                    if end - 1 - start > longestLength:
                        longestLength = end - 1 - start
                    start = hashWords[s[end]] + 1
                hashWords[s[end]] = end

            end += 1

        if end - 1 - start > longestLength:
            longestLength = end - 1 - start

        return longestLength + 1
        