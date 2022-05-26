class Solution(object):
    def subsets(self, nums):
        powerset = [[]]
        
        for num in nums:
            end = len(powerset)
            
            for i in range(end):
                powerset.append(powerset[i] + [num])
                
        return powerset
            
        