class Solution(object):
    def intToRoman(self, num):
        romanNums = [[1000, "M"], [900, "CM"], [500, "D"], [400, "CD"], [100, "C"], [90, "XC"], [50, "L"], [40, "XL"], [10, "X"], [9, "IX"], [5, "V"], [4, "IV"], [1, "I"]]
        res = []
        #search from beginning of array until current num > arrayVal
        #current num // arrayVal gives us how many times to use that char so append x times to out array
        #take modulos of current num % arrayVal to get new
        
        while num != 0:
            i = 0
            while i < len(romanNums):
                if num >= romanNums[i][0]:
                    rn = romanNums[i]
                    break
                i += 1
                    
            amountOfChars = num // rn[0]
            for i in range(amountOfChars):
                res.append(rn[1])
                
            num = num % rn[0]
            
            
        return "".join(res)
                    
                