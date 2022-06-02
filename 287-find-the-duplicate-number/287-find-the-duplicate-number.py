class Solution(object):
    def findDuplicate(self, nums):
        for value in nums:
            idxToMap = len(nums) - abs(value)
            if nums[idxToMap] < 0:
                return abs(value)
            else:
                nums[idxToMap] *= -1

        return -1
        