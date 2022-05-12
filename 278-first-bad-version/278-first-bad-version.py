# The isBadVersion API is already defined for you.
# @param version, an integer
# @return a bool
# def isBadVersion(version):

class Solution(object):
    def firstBadVersion(self, n):
        left = 1
        right = n
        firstBadVersion = float("inf")
        
        while left <= right:
            midVersion = (left + right) // 2
            
            if isBadVersion(midVersion):
                firstBadVersion = midVersion if midVersion < firstBadVersion else firstBadVersion
                right = midVersion - 1
            else:
                left = midVersion + 1
        
        return firstBadVersion
        