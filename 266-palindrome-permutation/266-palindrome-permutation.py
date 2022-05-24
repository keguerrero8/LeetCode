class Solution(object):
    def canPermutePalindrome(self, s):
        frequencyHash = {}
        for char in s:
            frequencyHash[char] = 1 + frequencyHash.get(char, 0)
        
        allowableUnevens = 1
        for frequency in frequencyHash.values():
            if frequency % 2 == 1:
                if allowableUnevens == 0: 
                    return False
                else:
                    allowableUnevens -= 1
        return True
                
        