class Solution(object):
    def subsets(self, nums, start = 0, base = None, powerSet = None):
        if powerSet is None:
            powerSet = [[]]
        if base is None:
            base = []
        if start == len(nums):
            return powerSet
        
        for i in range(start, len(nums)):
            newSet = base + [nums[i]]
            powerSet.append(newSet)
            self.subsets(nums, i+1, newSet, powerSet)
        
        return powerSet
        
#     def subsets(self, nums):
#         powerSet = [[]]
#         for num in nums:
#             length = len(powerSet)
#             for i in range(length):
#                 powerSet.append(powerSet[i]+[num])
                
#         return powerSet
        
        