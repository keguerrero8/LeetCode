class Solution(object):
    def subsets(self, nums):
        powerSet = [[]]
        #[1,2,3]
        #for 1
            #len = 1, [[], [1]]
        #for 2
            #len = 2, [[], [1], [2], [1,2]]
        #for 3
            #len = 4, [[], [1], [2], [1,2], [3], [1,3], [2,3], [1,2,3]]
            
        #Time and Space is O(n*2^n)
        for num in nums:
            length = len(powerSet)
            for i in range(length):
                powerSet.append(powerSet[i]+[num])
                
        return powerSet
        
        