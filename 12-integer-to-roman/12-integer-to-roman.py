class Solution(object):
    def intToRoman(self, num):
        #1994
        romans = [[1, "I"], [4, "IV"], [5, "V"], [9, "IX"], [10, "X"], [40, "XL"], [50, "L"], [90, "XC"], [100, "C"], [400, "CD"], [500, "D"], [900, "CM"], [1000, "M"]]
        
        res = []
        
        i = len(romans) - 1
        while num:
            if num >= romans[i][0]:
                j = num // romans[i][0]
                num = num % romans[i][0]
                k = 0
                while k < j:
                    res.append(romans[i][1])
                    k += 1
            i -= 1
            
        return "".join(res)
        