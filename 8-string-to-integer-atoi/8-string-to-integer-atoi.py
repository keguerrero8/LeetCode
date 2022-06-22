class Solution(object):
    def myAtoi(self, s):
        res = 0
        i = 0
        negative = 1
        MAX_INT = (2**31) - 1
        MIN_INT = -2**31
        
        #remove white spaces
        while i < len(s) and s[i] == " ":
            i += 1
            
        #check +/- symbol  
        if i < len(s) and s[i] == "-":
            i += 1
            negative = -1
        elif i < len(s) and s[i] == "+":
            i += 1
        
        #check for digits and MAX and MIN
        checker = set("0123456789")   
        while i < len(s) and s[i] in checker:
            if res > MAX_INT / 10 or (res == MAX_INT/10 and int(s[i]) > 7):
                return MAX_INT if negative == 1 else MIN_INT
            res = res*10 + int(s[i])
            i += 1

        return res*negative