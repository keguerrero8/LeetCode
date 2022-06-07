class Solution(object):
    def isSubsequence(self, s, t):
        if len(s) > len(t):
            return False
        i = 0
        for j in range(len(s)):
            if j != 0:
                i += 1
            while i < len(t) and t[i] != s[j]:
                i += 1
            if i == len(t):
                return False
        return True
        