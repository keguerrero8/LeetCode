class Solution(object):
    def isAnagram(self, s, t):
        hashMap = {}
        for char in s:
            if char not in hashMap:
                hashMap[char] = 1
            else:
                hashMap[char] += 1
                
        for char in t:
            if char in hashMap:
                if hashMap[char] == 0:
                    return False
                else:
                    hashMap[char] -= 1
            else:
                return False
            
        for value in hashMap.values():
            if value != 0:
                return False
        return True