class Solution(object):
    def isPalindrome(self, s):
        alphabet = {"a": True, "b": True, "c": True, "d": True, "e": True, "f":True,
                    "g": True, "h": True, "i": True, "j": True, "k": True, "l":True,
                    "m": True, "n": True, "o": True, "p": True, "q": True, "r":True,
                    "s": True, "t": True, "u": True, "v": True, "w": True, "x":True,
                    "y": True, "z": True, "0": True, "1": True, "2": True, "3": True,
                    "4": True, "5": True, "6": True, "7": True, "8": True, "9": True
                   }
        
        l = 0
        r = len(s) - 1
        
        while l <= r:
            while s[l].lower() not in alphabet and l < r:
                l += 1
                
            while s[r].lower() not in alphabet and r > l:
                r -= 1
            
            if r <= l:
                break
                
            if s[l].lower() != s[r].lower():
                return False
            
            l += 1
            r -= 1
                
        return True
        