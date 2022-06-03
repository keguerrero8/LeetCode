class Solution(object):
    def sortColors(self, nums):
        first, second, third = 0, 0, len(nums) - 1
        while second <= third:
            if nums[second] == 0:
                nums[second], nums[first] = nums[first], nums[second]
                first += 1
                second += 1
            elif nums[second] == 1:
                second += 1
            else:
                nums[second], nums[third] = nums[third], nums[second]
                third -= 1
            
        return nums

        