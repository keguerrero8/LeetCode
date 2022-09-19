class Solution(object):
    def longestPalindrome(self, s):
        if len(s) == 0:
            return 0
        if len(s) == 1:
            return s
        longestStart = 0
        longestEnd = 1
        for i in range(1, len(s)):
            if s[i] == s[i-1]:
                start, end = self.getPalindromeLength(i-1, i, s) 
                if end - start > longestEnd - longestStart:
                    longestStart = start
                    longestEnd = end
            if i+1 < len(s) and s[i-1] == s[i+1]:
                start, end = self.getPalindromeLength(i-1, i+1, s)
                if end - start > longestEnd - longestStart:
                    longestStart = start
                    longestEnd = end

        return s[longestStart:longestEnd]



    def getPalindromeLength(self, left, right, s):
        while s[left] == s[right]:
            left -= 1
            right += 1
            if left < 0 or right > len(s) - 1 or s[left] != s[right]:
                left += 1
                right -= 1
                break

        return left, right + 1
        