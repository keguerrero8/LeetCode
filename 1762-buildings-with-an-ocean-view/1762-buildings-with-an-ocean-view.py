class Solution(object):
    def findBuildings(self, heights):
        # stack = []
        # for i in reversed(range(len(heights))):
        #     if len(stack) == 0 or heights[i] > heights[stack[-1]]:
        #         stack.append(i)
        # result = []
        # for i in reversed(range(len(stack))):
        #     result.append(stack[i])
        # return result
        maxHeight = float("-inf")
        output = []
        for i in reversed(range(len(heights))):
            if heights[i] > maxHeight:
                maxHeight = heights[i]
                output.append(i)
                
        left, right = 0, len(output) - 1
        
        while left <= right:
            output[left], output[right] = output[right], output[left]
            left += 1
            right -= 1
            
        return output
        