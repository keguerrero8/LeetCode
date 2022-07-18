class Solution(object):
    def searchRange(self, nums, target):
        if len(nums) == 0:
            return [-1, -1]
        
        left = self.binSearch(nums, target, True)
        right = self.binSearch(nums, target, False)
        
        return [left, right]
        
    def binSearch(self, nums, target, leftBias):
        l, r = 0, len(nums) - 1
        i = -1
        while l <= r:
            m = (l + r) // 2
            
            if target > nums[m]:
                l = m + 1
            elif target < nums[m]:
                r = m - 1
            else:
                i = m
                if leftBias:
                    r = m - 1
                else:
                    l = m + 1
        return i
                