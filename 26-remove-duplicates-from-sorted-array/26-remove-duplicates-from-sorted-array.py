class Solution(object):
    def removeDuplicates(self, nums):
        if len(nums) == 1:
            return 1
        
        start = end = 1
        
        while start < len(nums) and end < len(nums):
            if nums[start] <= nums[start-1]:
                while end < len(nums) and nums[end] <= nums[start-1]:
                    end += 1
                if end == len(nums):
                    break
                nums[start], nums[end] = nums[end], nums[start]
            start += 1
            
        return start