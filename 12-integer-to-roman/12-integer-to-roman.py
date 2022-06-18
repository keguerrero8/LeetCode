class Solution(object):
    def intToRoman(self, num):
        symbols = [[1, "I"], [4, "IV"], [5, "V"], [9, "IX"], [10, "X"], [40, "XL"], [50, "L"], [90, "XC"], [100, "C"], [400, "CD"], [500, "D"], [900, "CM"], [1000, "M"]]
        intToRoman = []
        while num:
            for i in reversed(range(len(symbols))):
                if num >= symbols[i][0]:
                    intToRoman.append(symbols[i][1])
                    divisor = symbols[i][0]
                    break
                    
            num -= divisor
        
        #1994, ["M", ], 1994 - 1000 = 994
        #994, ["M", "CM", ], 994 - 900 = 94
        #94, ["M", "CM", "XC",], 94 - 90 = 4
        #4, ["M", "CM", "XC", "IV"], 4-4 = 0
        return "".join(intToRoman)
        