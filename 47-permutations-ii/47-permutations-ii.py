class Solution(object):
    def permuteUnique(self, nums):
        res = []
        perm = []
        count = { n:0 for n in nums}
        for n in nums:
            count[n] += 1
            
        def dfs():
            if len(perm) == len(nums):
                res.append(perm + [])
                return
            
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                    
                    dfs()
                    
                    count[n] += 1
                    perm.pop()
                    
        dfs()
        return res
            
            
#         res = []
#         self.permutationHelper(nums, res, 0)
#         return res
    
#     def permutationHelper(self, nums, res, start):
#         if start == len(nums):
#             res.append(nums[:])
#             return

#         for i in range(start, len(nums)):
#             if start != i and nums[start] == nums[i]:
#                 continue
#             nums[start], nums[i] = nums[i], nums[start]
#             self.permutationHelper(nums, res, start + 1)
#             nums[start], nums[i] = nums[i], nums[start]
            
        