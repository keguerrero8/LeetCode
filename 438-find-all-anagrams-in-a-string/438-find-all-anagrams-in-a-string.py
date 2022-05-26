class Solution(object):
    def findAnagrams(self, s, p):
        if len(p) > len(s):
            return []
        
        pHash = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0,
                 "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0,
                 "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0,
                 "v":0, "w":0, "x":0, "y":0, "z":0}
        
        sHash = {"a":0, "b":0, "c":0, "d":0, "e":0, "f":0, "g":0,
                 "h":0, "i":0, "j":0, "k":0, "l":0, "m":0, "n":0,
                 "o":0, "p":0, "q":0, "r":0, "s":0, "t":0, "u":0,
                 "v":0, "w":0, "x":0, "y":0, "z":0}
        
        for char in p:
            pHash[char] = 1 + pHash.get(char)
            
        for i in range(len(p)):
            sHash[s[i]] = 1 + sHash.get(s[i])
            
        start = 0
        anagramIdxs = []
        for i in range(len(p)-1, len(s)):
            if start != 0:
                sHash[s[start-1]] -= 1
                sHash[s[i]] += 1
                
            if pHash == sHash:
                anagramIdxs.append(start)
                
            start += 1
            
        return anagramIdxs
        