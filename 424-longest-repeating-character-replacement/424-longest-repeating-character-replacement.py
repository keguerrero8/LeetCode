class Solution(object):
    def characterReplacement(self, s, k):
        start = 0
        end = 0
        frequencyHash = {}
        longest = 1
        
        while end < len(s):
            window = end-start+1
            if s[end] not in frequencyHash:
                frequencyHash[s[end]] = 1
            else:
                frequencyHash[s[end]] += 1
            if window - self.mostFrequent(frequencyHash) <= k:
                longest = max(longest, window)
            else:
                while window - self.mostFrequent(frequencyHash) > k:
                    frequencyHash[s[start]] -= 1
                    start += 1
                    window = end-start+1
            end += 1
            
        return longest
    
    def mostFrequent(self, hashMap):
        maxFrequency = 1
        for frequency in hashMap.values():
            maxFrequency = max(maxFrequency, frequency)
            
        return maxFrequency