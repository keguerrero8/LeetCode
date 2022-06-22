class Solution(object):
    def dailyTemperatures(self, temperatures):
        res = [0 for i in range(len(temperatures))]
        stack = []
        
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                res[stack[-1]] = i - stack[-1]
                stack.pop()
            stack.append(i)
            
        return res
               
        