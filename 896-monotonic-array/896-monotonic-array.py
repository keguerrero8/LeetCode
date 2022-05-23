class Solution(object):
    def isMonotonic(self, nums):
        if len(nums) <= 2:
            return True
        
        j, k = 0, 1
        while k < len(nums) and nums[j] == nums[k]:
            j += 1
            k += 1
            
        if k == len(nums): return True
        monotonic = 1 if nums[k] > nums[j] else -1
        
        for i in range(k+1, len(nums)):
            if monotonic == 1:
                if nums[i] < nums[i-1]:
                    return False
            else:
                if nums[i] > nums[i-1]:
                    return False
        return True

        