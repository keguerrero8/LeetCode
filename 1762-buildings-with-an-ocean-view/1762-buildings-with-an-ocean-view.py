class Solution(object):
    def findBuildings(self, heights):
        stack = []
        for i in reversed(range(len(heights))):
            if len(stack) == 0 or heights[i] > heights[stack[-1]]:
                stack.append(i)
        result = []
        for i in reversed(range(len(stack))):
            result.append(stack[i])
        return result
        