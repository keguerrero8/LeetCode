class Solution(object):
    def rob(self, nums):
        if len(nums) == 1:
            return nums[0]
        
        with1Max = self.findMaxes(nums, 0, len(nums) - 1)
        without1Max = self.findMaxes(nums, 1, len(nums))
        
        return max(with1Max, without1Max)
    
    def findMaxes(self, nums, start, end):
        maxes = [0, 0]
        for i in range(start, end):
            right = max(maxes[0], maxes[1])  
            left = nums[i] + maxes[1]
            maxes[0] = left
            maxes[1] = right
            
        return max(maxes[0], maxes[1])