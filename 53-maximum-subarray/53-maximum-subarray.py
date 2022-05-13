class Solution(object):
    def maxSubArray(self, nums):
        maxSum = float("-inf")
        prevSum = 0
        
        for num in nums:
            currentSum = prevSum + num
            maxSum = currentSum if currentSum > maxSum else maxSum
            
            if num > currentSum:
                # maxSum = max(num, maxSum) 
                maxSum = max(num, maxSum)
                prevSum = num
            else:
                prevSum = currentSum
                
        return maxSum
        