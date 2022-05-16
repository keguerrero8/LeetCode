class Solution(object):
    def checkInclusion(self, s1, s2):
        if len(s1) > len(s2):
            return False
        
        s1Hash = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0,
                 "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0,
                 "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}
        s2Hash = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0, "h":0, "i":0, "j":0,
         "k":0, "l":0, "m":0, "n":0, "o":0, "p":0, "q":0, "r":0, "s":0, "t":0,
         "u":0, "v":0, "w":0, "x":0, "y":0, "z":0}
        
        for char in s1:
            s1Hash[char] += 1
        
        for i in range(0, len(s1)):
            s2Hash[s2[i]] += 1
            
        L = 0
        R = len(s1) - 1
        
        while R < len(s2):
            if L != 0:
                s2Hash[s2[L-1]] -= 1
                s2Hash[s2[R]] += 1
                
            if s1Hash == s2Hash:
                return True
            
            L += 1
            R += 1
            
        return False