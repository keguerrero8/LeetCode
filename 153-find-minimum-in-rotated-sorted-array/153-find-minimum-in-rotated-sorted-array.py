class Solution(object):
    def findMin(self, nums):
        start = 0
        end = len(nums)-1
        
        if nums[end] > nums[start] or len(nums) == 1:
            return nums[0]
        
        while start < end:
            mid = (start + end) // 2
            if nums[mid] > nums[start]:
                start = mid
            elif nums[mid] < nums[start]:
                end = mid
            else:
                return min(nums[end], nums[start])
        