class Solution(object):
    def strStr(self, haystack, needle):
        if needle == "":
            return 0
        
        if len(needle) > len(haystack):
            return -1
        
        i = 0
        while i < len(haystack):
            if haystack[i] == needle[0]:
                j = 0
                k = i
                while  k < len(haystack) and haystack[k] == needle[j]:
                    if j == len(needle) - 1:
                        return i
                    k += 1
                    j += 1
            i += 1
                
        return -1
        