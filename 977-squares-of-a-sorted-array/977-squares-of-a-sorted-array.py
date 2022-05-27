class Solution(object):
    def sortedSquares(self, nums):
        left = 0
        right = len(nums) - 1
        output = [0]*len(nums)
        outputPt = len(output) - 1
        
        while left <= right:
            leftVal = abs(nums[left])
            rightVal = abs(nums[right])
            
            if rightVal > leftVal:
                valueToInsert = rightVal*rightVal
                right -= 1
            else:
                valueToInsert = leftVal*leftVal
                left += 1
                
            output[outputPt] = valueToInsert
            outputPt -= 1
            
        return output