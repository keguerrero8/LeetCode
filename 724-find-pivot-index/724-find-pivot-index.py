class Solution(object):
    def pivotIndex(self, nums):
        total = sum(nums)
        leftSum = 0
        
        for i in range(len(nums)):
            if i != 0:
                leftSum += nums[i-1]
            total -= nums[i]
            if leftSum == total:
                return i
            
        return -1