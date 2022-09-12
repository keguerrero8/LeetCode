class Solution(object):
    def permuteUnique(self, nums):
        count = {n:0 for n in nums}
        for num in nums:
            count[num] += 1
        res = []
        perm = []
        
        def dfs():
            if len(perm) == len(nums):
                res.append(perm + [])
                return
            
            for n in count:
                if count[n] > 0:
                    perm.append(n)
                    count[n] -= 1
                    
                    dfs()
                    
                    perm.pop()
                    count[n] += 1
        dfs()         
        return res
                
            
        
            
            
        
        
                