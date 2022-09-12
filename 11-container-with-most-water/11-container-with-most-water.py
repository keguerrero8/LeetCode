class Solution(object):
    def maxArea(self, height):
        l, r = 0, len(height) - 1
        res = 0
        while l < r:
            currentWater = min(height[l], height[r]) * (r-l)
            res = max(res, currentWater)
            
            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
                
        return res
        