class Solution(object):
    def multiply(self, num1, num2):
        if "0" in [num1, num2]:
            return "0"
        
        res = [0]* (len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        
        for i1 in range(len(num1)):
            for i2 in range(len(num2)):
                digit = int(num1[i1]) * int(num2[i2])
                res[i1 + i2] += digit
                res[i1 + i2 + 1] += (res[i1 + i2] // 10)
                res[i1 + i2] = res[i1 + i2] % 10
            
        res, beg = res[::-1], 0
        while beg < len(res) and res[beg] == 0:
            beg += 1
            
        res = map(str, res[beg:])
        return "".join(res)
    
#         res = [-1]*(len(num1) + len(num2))

#         for i in reversed(range(len(num1))):
#             for j in reversed(range(len(num2))):
#                 rj = len(num2) - 1 - j
#                 ri = len(num1) - 1 - i
#                 idx = ri + rj
#                 resIdx = len(res) - 1 - idx
#                 product = str(int(num1[i])*int(num2[j]))
                
#                 for k in reversed(range(len(product))):
#                     if res[resIdx] == -1:
#                         res[resIdx] = str(int(product[k]))
#                     else:
#                         res[resIdx] = str(int(product[k]) + int(res[resIdx]))
#                     resIdx -= 1
#         startConc = 0
#         while res[startConc] == -1:
#             startConc += 1
            
#         return "".join(res[startConc:])
                
        