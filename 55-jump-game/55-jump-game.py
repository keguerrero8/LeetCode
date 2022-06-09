class Solution(object):
    def canJump(self, nums):
#         if nums[0] == 0:
#             return False
#         jumps = [0 for i in range(len(nums))]
#         jumps[0] = nums[0]
        
#         for i in range(1, len(jumps)):
#             if jumps[i-1] - 1 >= 0:
#                 jumps[i] = max(nums[i], jumps[i-1]-1)
#             else:
#                 return False
#         return True
    
        if len(nums) == 1:
            return True
        if nums[0] == 0:
            return False
        prevJump = nums[0]
        for i in range(1, len(nums)):
            if prevJump - 1 >= 0:
                prevJump = max(nums[i], prevJump-1)
            else:
                return False
        return True
        