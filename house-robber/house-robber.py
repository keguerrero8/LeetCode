class Solution(object):
    def rob(self, nums):
        maxArray = [0,0]

        for i in range(len(nums)):
            temp = max(maxArray[0], maxArray[1])
            maxArray[0] = nums[i] + maxArray[1]
            maxArray[1] = temp

        return max(maxArray[0], maxArray[1])
        