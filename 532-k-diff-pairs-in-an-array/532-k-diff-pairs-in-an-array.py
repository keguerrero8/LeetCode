class Solution(object):
    def findPairs(self, nums, k):
        frequencyHash = {}
        pairs = 0
        
        for i in range(len(nums)):
            if nums[i] not in frequencyHash:
                frequencyHash[nums[i]] = 1
            else:
                frequencyHash[nums[i]] += 1
                
        for key in frequencyHash.keys():
            if k > 0 and key + k in frequencyHash:
                pairs +=1
            elif k == 0 and frequencyHash[key] > 1:
                pairs += 1
                
        return pairs
                
        