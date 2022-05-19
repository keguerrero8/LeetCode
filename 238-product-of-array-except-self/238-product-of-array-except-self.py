class Solution(object):
    def productExceptSelf(self, nums):
        leftProducts = [0]*len(nums)
        rightProducts = [0]*len(nums)

        for i in range(len(nums)):
            if i == 0:
                leftProducts[i] = nums[i]
            else:
                leftProducts[i] = nums[i] * leftProducts[i-1]

        for i in reversed(range(len(nums))):
            if i == len(nums) - 1:
                rightProducts[i] = nums[i]
            else:
                rightProducts[i] = nums[i] * rightProducts[i+1]

        result = []
        for i in range(len(nums)):
            left = leftProducts[i-1] if i > 0 else 1
            right = rightProducts[i+1] if i < len(nums) - 1 else 1
            result.append(left*right)

        return result
        