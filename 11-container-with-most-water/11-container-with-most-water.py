class Solution(object):
    def maxArea(self, height):
        start, end = 0, len(height) - 1
        maxWater = float("-inf")
        
        while start < end:
            currentWaterArea = (end - start) * min(height[start], height[end])
            maxWater = max(currentWaterArea, maxWater)
            if height[start] < height[end]:
                start += 1
            else:
                end -= 1
        
        return maxWater
        