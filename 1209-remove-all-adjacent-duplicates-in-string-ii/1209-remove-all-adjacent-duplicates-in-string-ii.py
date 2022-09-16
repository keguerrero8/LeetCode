class Solution(object):
    def removeDuplicates(self, s, k):
        stack = []
        for i in range(len(s)):
            if stack and stack[-1][0] == s[i]:
                stack[-1][1] += 1
            else:
                stack.append([s[i], 1])
                
            if stack[-1][1] == k:
                stack.pop()
        res = []     
        for i in reversed(range(len(stack))):
            x = 0
            while x < stack[i][1]:
                res.append(stack[i][0])
                x += 1
        res = res[::-1]
        return "".join(res)
        