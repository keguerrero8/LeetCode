class Solution(object):
    def lengthOfLIS(self, nums):
        LIS = [1]*(len(nums))
        
        for i in reversed(range(len(nums) - 1)):
            for j in range(i+1, len(nums)):
                if nums[i] < nums[j]:
                    LIS[i] = max(LIS[i], LIS[j]+1)
                    
        longest = float("-inf")
        for i in range(len(LIS)):
            longest = max(LIS[i], longest)
            
        return longest