class Solution(object):
    def canJump(self, nums):
        if len(nums) == 1:
            return True
        
        isPossible = False
        IdxGoal = len(nums) - 1
        
        for i in reversed(range(len(nums)-1)):
            if nums[i] + i >= IdxGoal:
                IdxGoal = i
                isPossible = True
            else:
                isPossible = False
        
        return isPossible
        