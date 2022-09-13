class Solution(object):
    def multiply(self, num1, num2):
        if num1 == "0" or num2 == "0":
            return "0"
        res = [0]*(len(num1) + len(num2))
        num1, num2 = num1[::-1], num2[::-1]
        
        for i in range(len(num1)):
            for j in range(len(num2)):
                res[i+j] += int(num1[i])*int(num2[j])
                res[i+j+1] += (res[i+j] // 10)
                res[i+j] = res[i+j] % 10
        
        res = res[::-1]
        for i in range(len(res)):
            res[i] = str(res[i])
        i = 0
        while i < len(res) and res[i] == "0":
            i += 1
            
        return "".join(res)[i:]
        