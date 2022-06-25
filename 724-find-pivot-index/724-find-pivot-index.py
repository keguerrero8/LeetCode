class Solution(object):
    def pivotIndex(self, nums):
        left = [0]*len(nums)
        right = [0]*len(nums)
        
        for i in range(1, len(nums)):
            left[i] = left[i-1] + nums[i-1]
        
        for i in reversed(range(len(nums)-1)):
            right[i] = right[i+1] + nums[i+1]
            
        for i in range(len(nums)):
            if right[i] == left[i]:
                return i
            
        return -1