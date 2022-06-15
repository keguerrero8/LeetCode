class Solution(object):
    def reverse(self, x):
        if x == 0:
            return 0
        isNegative = False
        if x < 0:
            isNegative = True
            x *= -1
            
        i = 0
        reverse = []
        valueToReverse = x
        while True:
            digitRem = valueToReverse % 10
            reverse.append(digitRem)
            valueToReverse -= digitRem
            if valueToReverse == 0:
                break
            valueToReverse = valueToReverse / 10
            i += 1
            
        #check for leading 0s
        j = 0
        while reverse[j] == 0:
            i -= 1
            j += 1
        
        reversedValue = 0
        for k in range(j, len(reverse)):
            digit = reverse[k]
            reversedValue += (10**i)*digit
            i -= 1
            
        if reversedValue > 2**31:
            return 0
            
        return reversedValue if not isNegative else -1*reversedValue
        