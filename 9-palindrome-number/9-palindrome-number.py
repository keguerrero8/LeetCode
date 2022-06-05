class Solution(object):
    def isPalindrome(self, x):
        if x < 0:
            return False
        stringRep = str(x)
        start, end = 0, len(stringRep) - 1
        while start <= end:
            if stringRep[start] != stringRep[end]:
                return False
            start += 1
            end -= 1
        return True