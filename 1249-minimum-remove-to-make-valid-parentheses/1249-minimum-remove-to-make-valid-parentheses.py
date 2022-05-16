class Solution(object):
    def minRemoveToMakeValid(self, s):
        openParenthesis = "("
        closingParenthesis = ")"
        stack = []
        
        for i in range(len(s)):
            if s[i] == closingParenthesis:
                if len(stack) == 0 or s[stack[-1]] != openParenthesis:
                    stack.append(i)
                else:
                    stack.pop()
            elif s[i] == openParenthesis:
                stack.append(i)
                
        if len(stack) == 0:
            return s
        
        stackPt = 0
        result = []
        
        for i in range(len(s)):
            if stackPt < len(stack) and i == stack[stackPt]:
                stackPt += 1
                continue
            result.append(s[i])
            
        return "".join(result) if result else ""
        