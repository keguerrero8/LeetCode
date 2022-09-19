class Solution(object):
    def isValid(self, s):
        parenthesis = {")":"(", "}":"{", "]":"["}
        stack = []
        for char in s:
            if char not in parenthesis:
                stack.append(char)
            else:
                if len(stack) > 0 and stack[-1] == parenthesis[char]:
                    stack.pop()
                else:
                    return False
        return len(stack) == 0
        