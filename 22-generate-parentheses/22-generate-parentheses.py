class Solution(object):
    def generateParenthesis(self, n, pairs = None, openP = 0, closeP = 0, stack = None):
        if pairs == None:
            pairs = []
            stack = []
            
        if openP == n and closeP == n:
            pairs.append("".join(stack))
            return pairs
        
        if openP >= closeP and openP < n:
            stack.append("(")
            self.generateParenthesis(n, pairs, openP+1, closeP, stack)
            stack.pop()
            
        if closeP < openP and closeP < n:
            stack.append(")")
            self.generateParenthesis(n, pairs, openP, closeP+1, stack)
            stack.pop()
            
        return pairs