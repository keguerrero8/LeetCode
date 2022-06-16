class Solution(object):
    def generateParenthesis(self, n):
        result = []
        stack = []
        self.generateParenthesisHelper(0, 0, result, stack, n)
        return result
    
    def generateParenthesisHelper(self, openN, closeN, result, stack, n):
        if openN == closeN == n:
            result.append("".join(stack))
            return
        
        if closeN < openN:
            stack.append(")")
            self.generateParenthesisHelper(openN, closeN+1, result, stack, n)
            stack.pop()
            
        if openN < n:
            stack.append("(")
            self.generateParenthesisHelper(openN + 1, closeN, result, stack, n)
            stack.pop()
            
        return
        