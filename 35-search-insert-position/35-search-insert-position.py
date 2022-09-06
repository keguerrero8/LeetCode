class Solution(object):
    def searchInsert(self, nums, target):
        l, r = 0, len(nums) - 1
        
        while l <= r:
            mid = (l + r) // 2
            
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                l = mid + 1
            else:
                r = mid - 1
        
        if l > r:
            return r + 1
        
        if r < l:
            return l - 1 if l-1 > 0 else 0
        
        
        