class Solution(object):
    def maxDepth(self, s):
        stack = []
        res = 0
        
        for i in range(len(s)):
            res = max(res, len(stack))
            
            if s[i] == "(":
                stack.append(s[i])
            elif s[i] == ")" and stack[-1] == "(":
                stack.pop()
                
        return res