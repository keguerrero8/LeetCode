class Solution(object):
    # def fib(self, n, hashMap = None):
    #     if hashMap == None:
    #         hashMap = {0:0, 1:1}
    #     if n in hashMap:
    #         return hashMap[n]
    #     else:
    #         hashMap[n] = fib(n-1, hashMap) + fib(n-2, hashMap)
    #     return hashMap[n]
    
    def fib(self, n):
        fibNums = [0, 1]
        
        if n == 1:
            return 1
        elif n == 0:
            return 0
        
        for i in range(2, n+1):
            currentFib = fibNums[0] + fibNums[1]
            fibNums[0] = fibNums[1]
            fibNums[1] = currentFib
            
        return currentFib
        
        