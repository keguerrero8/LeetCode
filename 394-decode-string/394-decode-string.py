class Solution(object):
    def decodeString(self, s):
        stack = []
        
        for i in range(len(s)):
            if s[i] != "]":
                stack.append(s[i])
            else:
                substr = ""
                while stack[-1] != "[":
                    substr = stack.pop() + substr
                stack.pop()
                
                k = ""
                while stack and stack[-1].isdigit():
                    k = stack.pop() + k
                stack.append(int(k)*substr)
                
        return "".join(stack)
    
    
#     def decodeString(self, s):
#         st, pt = self.decodeHelper(s, 0)
#         return st
    
#     def decodeHelper(self, s, i):
#         res = []
        
#         while i < len(s) and s[i] != "]":
#             if s[i] in "abcdefghijklmnopqrstuvwxyz":
#                 res.append(s[i])
#             else:
#                 start = i
#                 while s[i+1] != "[":
#                     i += 1
#                 x = 0
#                 partString, j = self.decodeHelper(s, i+2)
#                 while x < int(s[start:i+1]):
#                     res.append(partString)
#                     x += 1
#                 i = j
#             i += 1
            
#         return "".join(res), i
            
        
                    
        