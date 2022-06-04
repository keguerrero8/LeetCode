class Solution(object):
    def characterReplacement(self, s, k):
        start, end = 0, 0
        frequencyHash = {s[0]: 1}
        longest = 1
        
        while end < len(s):
            currentLength = end - start + 1
            maxLetterFrequency = self.getMaxLetterFrequency(frequencyHash)
            
            if currentLength - maxLetterFrequency <= k:
                longest = max(longest, currentLength)
                end += 1
                if end < len(s):
                    frequencyHash[s[end]] = 1 + frequencyHash.get(s[end], 0)
            else:
                frequencyHash[s[start]] -= 1
                start += 1
                 
        return longest
                
            
    def getMaxLetterFrequency(self, frequencyHash):
        maxFrequency = 0
        for frequency in frequencyHash.values():
            maxFrequency = max(maxFrequency, frequency)
        return maxFrequency
        