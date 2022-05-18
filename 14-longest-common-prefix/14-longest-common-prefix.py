class Solution(object):
    def longestCommonPrefix(self, strs):
        if len(strs) == 1:
            return strs[0]
        prefix = []
        isEndWord = False
        idx = 0
        
        while True:
            if idx < len(strs[0]):
                prev = strs[0][idx]
            else:
                break
            for i in range(1, len(strs)):
                if idx >= len(strs[i]) or strs[i][idx] != prev:
                    isEndWord = True
                    break
                    
            if isEndWord:
                break
                
            prefix.append(prev)
            idx += 1
            
        return "".join(prefix) if len(prefix) > 0 else ""
                
                
        