class Solution(object):
    def permute(self, nums, res = None, start = 0):
        if res == None:
            res = []
            
        if start > len(nums) - 1:
            res.append(nums + [])
            return
        
        for i in range(start, len(nums)):
            nums[start], nums[i] = nums[i], nums[start]
            self.permute(nums, res, start + 1)
            nums[start], nums[i] = nums[i], nums[start]
            
        return res
        
        