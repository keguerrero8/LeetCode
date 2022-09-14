class Solution(object):
    def jump(self, nums):
        jumps = 0
        l = r = 0
        while r < len(nums) - 1:
            farthest = 0
            for j in range(l, r + 1):
                farthest = max(farthest, nums[j] + j)
            
            jumps += 1
            l = r + 1
            r = farthest
            
        return jumps