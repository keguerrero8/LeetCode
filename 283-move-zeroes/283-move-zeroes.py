class Solution(object):
    def moveZeroes(self, nums):
        l = 0
        
        for r in range(len(nums)):
            if nums[r]:
                nums[r], nums[l] = nums[l], nums[r]
                l += 1
                
        return nums
                
        