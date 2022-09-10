class Solution(object):
    def subsetsWithDup(self, nums):
        res = [[]]
        nums.sort()
        prev = 0
        for i in range(len(nums)):
            end = len(res)
            if i > 0 and nums[i] == nums[i-1]:
                pass
            else:
                prev = 0
                
            for j in range(prev, end):
                copy = res[j] + [nums[i]]
                res.append(copy)
            prev = end
            
        return res     
            
        