class Solution(object):
    #dividend = 93706 and divisor is 157
    #-2147483648 to 2147483647
    def divide(self, dividend, divisor):
        res = 0
        dv = abs(dividend)
        
        while dv >= abs(divisor):
            mul = 1
            currentDivisor = abs(divisor)
            while currentDivisor + currentDivisor <= dv:
                mul += mul
                currentDivisor += currentDivisor
            res += mul
            dv -= currentDivisor
        if (dividend < 0 and divisor > 0) or (dividend > 0 and divisor < 0):
            res = 0 - res
        if res > 2147483647: return 2147483647
        if res < -2147483648: return -2147483648
        return res 
        